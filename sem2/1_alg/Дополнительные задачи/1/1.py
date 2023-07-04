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


def inOrder(root):
    if root == -1:
        return
    inOrder(root.l)
    out.write(str(root.val) + " ")
    inOrder(root.r)


def preOrder(root):
    if root == -1:
        return
    out.write(str(root.val) + " ")
    preOrder(root.l)
    preOrder(root.r)


def postOrder(root):
    if root == -1:
        return
    postOrder(root.l)
    postOrder(root.r)
    out.write(str(root.val) + " ")


n = int(lines[0])
inputs = []

for i in range(n):
    arr = list(map(int, lines[i+1].split()))
    inputs.append(arr)
root = Node(inputs[0][0])
root.l = insert(inputs[0][1])
root.r = insert(inputs[0][2])
inOrder(root)
out.write("\n")
preOrder(root)
out.write("\n")
postOrder(root)

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
