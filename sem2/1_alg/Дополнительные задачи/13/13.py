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
        self.height = 0


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

    el.height = max(getHeight(el.l), getHeight(el.r)) + 1

    nodes[i-1] = el

    return el


def getHeight(node):
    if not node:
        return -1

    return node.height


def getBalance(node):
    if not node:
        return 0

    return getHeight(node.l) - getHeight(node.r)


def rotateLeft(x):
    y = x.r

    x.r = y.l
    y.l = x

    x.height = 1 + max(getHeight(x.l), getHeight(x.r))
    y.height = 1 + max(getHeight(y.l), getHeight(y.r))

    return y


antwort = []


def printOut(node, count):
    if node:
        antwort.append([node.val])
    else:
        return 0
    count2 = 0
    count3 = 0

    if node.l:
        antwort[count].append(count + 2)
        count2 = printOut(node.l, count + 1)
    else:
        antwort[count].append(0)
    if node.r:
        if count2:
            count3 = printOut(node.r, count2 + 1)
            antwort[count].append(count2+2)
        else:
            count3 = printOut(node.r, count + 1)
            antwort[count].append(count+2)
    else:
        antwort[count].append(0)

    return max(count, count2, count3)


n = int(lines[0])
nodes = [0] * n
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
root = rotateLeft(root)
printOut(root, 0)
for i in range(len(antwort)):
    out.write(" ".join(map(str, antwort[i])) + "\n")

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
