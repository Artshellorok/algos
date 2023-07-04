import random
import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
f = open('output.txt', 'w')
lines = file.readlines()


def countSort(div):
    global a
    n = len(a)

    out = [0] * n
    count = [0] * 10

    for i in range(n):
        index = a[i] // div
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i-1]

    for i in range(n-1, -1, -1):
        index = a[i] // div
        out[count[index % 10] - 1] = a[i]
        count[index % 10] -= 1
        i -= 1

    a = out[:]


def radixSort():
    global a
    maxi = max(a)
    div = 1
    while maxi / div >= 1:
        countSort(div)
        div *= 10


n = int(lines[0])
a = []
for i in range(n):
    a.append(random.randint(0, n**3-1))
radixSort()
f.write(" ".join(list(map(str, a))))
f.close()

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
