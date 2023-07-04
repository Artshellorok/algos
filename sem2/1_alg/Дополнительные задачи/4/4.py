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


def inOrder(node, x):
    global k
    if node is None:
        return
    else:
        if node.val == -1:
            return
    inOrder(node.l, x)
    k += 1
    if k == x:
        out.write(str(node.val) + "\n")
        return
    inOrder(node.r, x)


i = 0
line = lines[i]
root = Node(-1)
while True:
    act, x = line.split()
    x = int(x)
    if act == "+":
        insert(root, x)
    else:
        k = 0
        inOrder(root, x)
    if i == len(lines)-1:
        break
    i += 1
    line = lines[i]

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
