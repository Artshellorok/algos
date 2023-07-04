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
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key, node=None):
        threshold = 1
        if not node:
            if not self.root:
                node = Node(key)
                self.root = node
                return self.root
            return Node(key)

        if (key < node.val):
            node.l = self.insert(key, node.l)
        else:
            node.r = self.insert(key, node.r)

        node.height = max(self.getHeight(node.l), self.getHeight(node.r)) + 1
        balance = self.getBalance(node)

        if balance > threshold:
            if self.getBalance(node.l) >= 0:
                node = self.rotateRight(node)
            else:
                node = self.rotateLeftRight(node)
        elif balance < -threshold:
            if self.getBalance(node.r) <= 0:
                node = self.rotateLeft(node)
            else:
                node = self.rotateRightLeft(node)

        self.root = node

        return node

    def exists(self, key, node=None):
        if not node:
            node = self.root
        if key == node.val:
            return "true"
        elif key < node.val:
            if node.l:
                return self.exists(key, node.l)
        elif key > node.val:
            if node.r:
                return self.exists(key, node.r)
        return "false"

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

    def prev(self, key, node=None):
        if node == None:
            node = self.root
        if node.val >= key:
            if node.l:
                return self.prev(key, node.l)
            else:
                return "none"
        else:
            if node.r:
                var = self.prev(key, node.r)
                if var == "none" and node.val < key:
                    return node.val
                return var
            else:
                if node.val < key:
                    return node.val
                return "none"

    def getMinValueNode(self, node):
        if node is None or node.l is None:
            return node

        return self.getMinValueNode(node.l)

    def delete(self, key, node=None):
        if not node:
            return node

        elif key < node.val:
            node.l = self.delete(key, node.l)

        elif key > node.val:
            node.r = self.delete(key, node.r)

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
            node.r = self.delete(temp.val, node.r)

        if node is None:
            self.root = node
            return node

        node.height = max(self.getHeight(node.l), self.getHeight(node.r)) + 1

        balance = self.getBalance(node)

        if balance > 1 and self.getBalance(node.l) >= 0:
            self.root = self.rotateRight(node)
            return self.root

        if balance < -1 and self.getBalance(node.r) <= 0:
            self.root = self.rotateLeft(node)
            return self.root

        if balance > 1 and self.getBalance(node.l) < 0:
            self.root = self.rotateLeftRight(node)
            return self.root

        if balance < -1 and self.getBalance(node.r) > 0:
            self.root = self.rotateRightLeft(node)
            return self.root

        self.root = node

        return node

    def rotateRight(self, x):
        y = x.l

        x.l = y.r
        y.r = x

        x.height = 1 + max(self.getHeight(x.l), self.getHeight(x.r))
        y.height = 1 + max(self.getHeight(y.l), self.getHeight(y.r))

        return y

    def rotateLeft(self, x):
        y = x.r

        x.r = y.l
        y.l = x

        x.height = 1 + max(self.getHeight(x.l), self.getHeight(x.r))
        y.height = 1 + max(self.getHeight(y.l), self.getHeight(y.r))

        return y

    def rotateLeftRight(self, node):
        node.l = self.rotateLeft(node.l)

        return self.rotateRight(node)

    def rotateRightLeft(self, node):
        node.r = self.rotateRight(node.r)

        return self.rotateLeft(node)

    def getBalance(self, node):
        if not node:
            return 0

        return self.getHeight(node.l) - self.getHeight(node.r)

    def getHeight(self, node):
        if not node:
            return -1

        return node.height


def maxi(root, k):
    curr = root
    Klargest = None
    count = 0

    while (curr != None):
        if (curr.r == None):
            count += 1
            if (count == k):
                Klargest = curr

            curr = curr.l

        else:
            succ = curr.r

            while (succ.l != None and
                   succ.l != curr):
                succ = succ.l

            if (succ.l == None):
                succ.l = curr
                curr = curr.r
            else:
                succ.l = None
                count += 1
                if (count == k):
                    Klargest = curr

                curr = curr.l

    return Klargest


tree = AVLTree()
n = int(lines[0])
for i in range(n):
    act, x = lines[i+1].split()
    x = int(x)
    if act == "+1":
        tree.insert(x, tree.root)
    elif act == "0":
        if tree.root == None:
            out.write("none\n")
        else:
            out.write(str(maxi(tree.root, x).val) + "\n")
    elif act == "-1":
        tree.delete(x, tree.root)

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
