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


def isBST(node, mini, maxi):
    if node.val < mini or node.val > maxi:
        return False
    if node.l != 0:
        erste = isBST(node.l, mini, node.val - 1)
    else:
        erste = True

    if node.r != 0:
        zweite = isBST(node.r, node.val+1, maxi)
    else:
        zweite = True

    return erste and zweite


n = int(lines[0])
if n == 0:
    out.write("YES")
else:
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

    if isBST(root, -(10**9+1), 10**9+1):
        out.write("YES")
    else:
        out.write("NO")

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
