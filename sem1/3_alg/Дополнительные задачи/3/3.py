import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()


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


n, k = map(int, lines[0].split())

arr = list(map(int, lines[1].split()))
a = []
m = {}
for i in range(n):
    a.append([arr[i], i])
    arr[i] = [arr[i], i]
    if arr[i][0] not in m:
        m[arr[i][0]] = [i]
    else:
        m[arr[i][0]].append(i)

quickSort(0, n-1)

for i in range(n):
    if len(m[a[i][0]]) > 1:
        count = 0
        for j in range(len(m[a[i][0]])):
            ind = m[a[i][0]][j]
            if ind != -1:
                if abs(ind - i) == k or abs(ind - i) == 0:
                    m[a[i][0]][j] = -1
                    count += 1
        if not count:
            open("output.txt", 'w').write("НЕТ")
            print("Время выполнения: " +
                  str(time.perf_counter() - t_start) + " секунд")
            print("Использование памяти: " +
                  str(tracemalloc.get_traced_memory()[1]) + " байт")
            tracemalloc.stop()
            exit()

    else:
        if abs(a[i][1] - i) == k or abs(a[i][1] - i) == 0:
            continue
        else:
            open("output.txt", 'w').write("НЕТ")
            print("Время выполнения: " +
                  str(time.perf_counter() - t_start) + " секунд")
            print("Использование памяти: " +
                  str(tracemalloc.get_traced_memory()[1]) + " байт")
            tracemalloc.stop()
        exit()
open("output.txt", 'w').write("ДА")

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
