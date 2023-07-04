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


def get(node, x):
    if node.val <= x:
        if node.r:
            return get(node.r, x)
        else:
            return 0
    else:
        if node.l:
            var = get(node.l, x)
            if var == 0 and node.val > x:
                return node.val
            return var
        else:
            if node.val > x:
                return node.val
            return 0


line = lines[0]
root = Node(-1)
i = 0
while True:
    act, x = line.split()
    x = int(x)
    if act == "+":
        insert(root, x)
    else:
        out.write(str(get(root, x)) + "\n")

    if i == len(lines)-1:
        break
    i += 1
    line = lines[i]

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
