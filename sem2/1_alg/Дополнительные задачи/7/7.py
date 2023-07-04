import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")


class Node:
    def __init__(self, val):
        self.l = -1
        self.r = -1
        self.val = val


def insert(i):
    k, l, r = inputs[i]
    el = Node(k)
    if l != - 1:
        el.l = insert(l)
    else:
        el.l = -1

    if r != -1:
        el.r = insert(r)
    else:
        el.r = -1
    return el


def isBST(node, mini, maxi):
    if node.val < mini or node.val > maxi:
        return False
    if node.l != -1:
        erste = isBST(node.l, mini, node.val - 1)
    else:
        erste = True

    if node.r != -1:
        zweite = isBST(node.r, node.val, maxi)
    else:
        zweite = True

    return erste and zweite


n = int(lines[0])
inputs = []

for i in range(n):
    arr = list(map(int, lines[i+1].split()))
    inputs.append(arr)
if n == 0:
    out.write("CORRECT")
else:
    root = Node(inputs[0][0])
    if inputs[0][1] == -1:
        root.l = -1
    else:
        root.l = insert(inputs[0][1])
    if inputs[0][2] == -1:
        root.r = -1
    else:
        root.r = insert(inputs[0][2])
    if isBST(root, - (2**32+1), 2**32+1):
        out.write("CORRECT")
    else:
        out.write("INCORRECT")


print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
