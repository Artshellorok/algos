import time
import tracemalloc


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.val = val


def insert(node, el):
    val = node.val
    if el == val:
        return
    if val == -1:
        node.val = el
        return
    if el >= val:
        if node.r:
            insert(node.r, el)
        else:
            node.r = Node(el)
    else:
        if node.l:
            insert(node.l, el)
        else:
            node.l = Node(el)


def next(node, x):
    if node.val <= x:
        if node.r:
            return next(node.r, x)
        else:
            return "none"
    else:
        if node.l:
            var = next(node.l, x)
            if var == "none" and node.val > x:
                return node.val
            return var
        else:
            if node.val > x:
                return node.val
            return "none"


def prev(node, x):
    if node.val >= x:
        if node.l:
            return prev(node.l, x)
        else:
            return "none"
    else:
        if node.r:
            var = prev(node.r, x)
            if var == "none" and node.val < x:
                return node.val
            return var
        else:
            if node.val < x:
                return node.val
            return "none"


def exists(node, x):
    val = node.val
    if val == x:
        return "true"
    if x >= val:
        if node.r:
            return exists(node.r, x)
        else:
            return "false"
    else:
        if node.l:
            return exists(node.l, x)
        else:
            return "false"


def getMinimumKey(curr):
    while curr.l:
        curr = curr.l
    return curr


def delete(root, x):
    parent = None

    curr = root

    while curr and curr.val != x:
        parent = curr

        if x < curr.val:
            curr = curr.l
        else:
            curr = curr.r

    if curr is None:
        return root

    if curr.l is None and curr.r is None:
        if curr != root:
            if parent.l == curr:
                parent.l = None
            else:
                parent.r = None
        else:
            root = None

    elif curr.l and curr.r:
        successor = getMinimumKey(curr.r)
        val = successor.val
        delete(root, successor.val)
        curr.val = val

    else:
        if curr.l:
            child = curr.l
        else:
            child = curr.r

        if curr != root:
            if curr == parent.l:
                parent.l = child
            else:
                parent.r = child
        else:
            root = child

    return root


tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

i = 0
line = lines[i]
root = Node(-1)
while True:
    act, x = line.split()
    x = int(x)
    if act == "insert":
        insert(root, x)
    elif act == "exists":
        out.write(str(exists(root, x)) + "\n")
    elif act == "delete":
        root = delete(root, x)
    elif act == "next":
        out.write(str(next(root, x)) + "\n")
    else:
        out.write(str(prev(root, x)) + "\n")
    if i == len(lines)-1:
        break
    i += 1
    line = lines[i]

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
