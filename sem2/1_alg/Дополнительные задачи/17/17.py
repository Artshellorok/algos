import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.val = val
        self.sum = val


class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return self.root

        self.root = self.splay(self.root, key)

        if self.root.val == key:
            return self.root

        node = Node(key)
        if self.root.val > key:
            node.r = self.root
            node.l = self.root.l
            self.root.l = None
        else:
            node.l = self.root
            node.r = self.root.r
            self.root.r = None

        self.root = node

        return node

    def splay(self, root, key):
        if root is None or root.val == key:
            return root

        if root.val > key:
            if root.l is None:
                return root
            if root.l.val > key:
                root.l.l = self.splay(root.l.l, key)
                root = self.rotateRight(root)
            elif root.l.val < key:
                root.l.r = self.splay(root.l.r, key)
                if root.l.r is not None:
                    root.l = self.rotateLeft(root.l)
            return (root.l is None) and root or self.rotateRight(root)
        else:
            if root.r is None:
                return root
            if root.r.val > key:
                root.r.l = self.splay(root.r.l, key)
                if root.r.l:
                    root.r = self.rotateRight(root.r)
            elif root.r.val < key:
                root.r.r = self.splay(root.r.r, key)
                root = self.rotateLeft(root)
            return (root.r is None) and root or self.rotateLeft(root)

    # def exists(self, key, node=None):
    #     if not node:
    #         if self.root:
    #             node = self.root
    #         else:
    #             return "Not found"
    #     if key == node.val:
    #         return "Found"
    #     elif key < node.val:
    #         if node.l:
    #             return self.exists(key, node.l)
    #     elif key > node.val:
    #         if node.r:
    #             return self.exists(key, node.r)
    #     return "Not found"
    def exists(self, key):
        res = self.splay(self.root, key)
        if self.root:
            self.root = res
            return "Found" if res.val == key else "Not found"
        else:
            return "Not found"

    def getMinValueNode(self, node):
        if node is None or node.l is None:
            return node

        return self.getMinValueNode(node.l)

    def delete(self, key, node=None, parent=None):
        if not node:
            return node

        elif key < node.val:
            node.l = self.delete(key, node.l, node)

        elif key > node.val:
            node.r = self.delete(key, node.r, node)

        else:
            # cases in which we delete a node with one child
            if node.l is None:
                temp = node.r
                node = None
                self.root = temp
                return temp

            elif node.r is None:
                temp = node.l
                node = None
                self.root = temp
                return temp
            # cases in which a node with 2 children is encountered
            temp = self.getMinValueNode(node.r)
            node.val = temp.val
            node.r = self.delete(temp.val, node.r, node)

        if node is None:
            self.root = node
            return node

        if parent:
            mem = parent.val
            self.delete(mem, self.root)
            self.root = self.splay(self.root, mem)
        else:
            self.root = node

        return node

    def next(self, key, node=None):
        if node == None:
            node = self.root
        if node.val <= key:
            if node.r:
                return self.next(key, node.r)
            else:
                return "none"
        else:
            if node.l:
                var = self.next(key, node.l)
                if var == "none" and node.val > key:
                    return node.val
                return var
            else:
                if node.val > key:
                    return node.val
                return "none"

    def rotateRight(self, x):
        y = x.l

        x.l = y.r
        y.r = x

        return y

    def rotateLeft(self, x):
        y = x.r

        x.r = y.l
        y.l = x

        return y


tree = SplayTree()
n = int(lines[0])
m = 1000000001
add = 0
for i in range(n):
    inputs = lines[i+1].split()
    if len(inputs) == 3:
        act, x, y = inputs
        y = int(y)
    else:
        act, x = inputs
    x = int(x)
    if act == "+":
        tree.insert((x+add) % m)
    elif act == "?":
        out.write(tree.exists((x+add) % m) + "\n")
    elif act == "-":
        tree.delete((x+add) % m, tree.root)
    elif act == "s":
        summ = 0
        el = (x+add) % m
        el2 = (y+add) % m
        if tree.root != None:
            while el != "none":
                if el <= el2:
                    if tree.exists(el) == "Found":
                        summ += el
                    el = tree.next(el)
                else:
                    break
            add = summ
            out.write(str(summ) + "\n")
        else:
            out.write("Not found\n")

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
