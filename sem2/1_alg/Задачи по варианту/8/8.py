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


def depth(node):
    erste = -1
    zweite = -1
    if node.l:
        erste = depth(node.l)
    if node.r:
        zweite = depth(node.r)
    if erste == zweite == -1:
        return 1
    return max(zweite, erste) + 1


n = int(lines[0])
inputs = []

for i in range(n):
    arr = list(map(int, lines[i+1].split()))
    inputs.append(arr)

root = Node(inputs[0][0])
if inputs[0][1] == 0:
    root.l = 0
else:
    root.l = insert(inputs[0][1])
if inputs[0][2] == 0:
    root.r = 0
else:
    root.r = insert(inputs[0][2])
out.write(str(depth(root)))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
