import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt', 'r')
lines = file.readlines()
f = open('output.txt', 'w')


def quickSort(l, r):
    i = l
    j = r
    pivot = a[(i+j)//2][0]
    while i <= j:
        while a[i][0] < pivot:
            i += 1
        while a[j][0] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if j > l:
        quickSort(l, j)
    if i < r:
        quickSort(i, r)


n, k = list(map(int, lines[0].split()))

a = []

for i in range(n):
    x, y = map(int, lines[i+1].split())
    dist = x**2 + y**2
    a.append([dist, x, y])
quickSort(0, n-1)
for i in range(k):
    string = f"[{a[i][1]},{a[i][2]}]"
    f.write(string)
    if i != k-1:
        f.write(',')

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
