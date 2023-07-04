import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")


class Node:
    def __init__(self, val):
        self.l = 0
        self.r = 0
        self.val = val


def insert(i):
    k, l, r = inputs[i-1]
    el = Node(k)
    if l != 0:
        el.l = insert(l)
    else:
        el.l = 0

    if r != 0:
        el.r = insert(r)
    else:
        el.r = 0
    return el


def countNodes(node):
    count = 1

    if node.l:
        count += countNodes(node.l)
    if node.r:
        count += countNodes(node.r)

    return count


def removeSubtree(node, key, prev=None, richtung=None):
    val = node.val
    if key == val:
        count = countNodes(node)
        if richtung == 'l':
            prev.l = None
        if richtung == 'r':
            prev.r = None
        return count
    if key < val:
        if node.l:
            return removeSubtree(node.l, key, node, 'l')
        else:
            return 0
    if key > val:
        if node.r:
            return removeSubtree(node.r, key, node, 'r')
        else:
            return 0


n = int(lines[0])
inputs = []
node_count = 0
for i in range(n):
    arr = list(map(int, lines[i+1].split()))
    inputs.append(arr)
    node_count += 1

root = Node(inputs[0][0])
if inputs[0][1] == 0:
    root.l = 0
else:
    root.l = insert(inputs[0][1])
if inputs[0][2] == 0:
    root.r = 0
else:
    root.r = insert(inputs[0][2])
m = int(lines[n+1])
queue = list(map(int, lines[n+2].split()))
for i in range(m):
    node_count -= removeSubtree(root, queue[i])
    out.write(str(node_count) + "\n")

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
