import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()


def quick_sort(l, r):
    i = l
    j = r
    pivot = arr[(i+j)//2][0]
    while i <= j:
        while arr[i][0] < pivot:
            i += 1
        while arr[j][0] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if j > l:
        quick_sort(l, j)
    if i < r:
        quick_sort(i, r)


s, p = map(int, lines[0].split())
arr = []

for i in range(s):
    a, b = map(int, lines[i+1].split())
    arr.append([a, "b"])
    arr.append([b, "e"])
d = list(map(int, lines[s+1].split()))

for i in range(p):
    arr.append([d[i], "el"])

quick_sort(0, s*2+p-1)

ans = {}
count = 0

for i in range(len(arr)):
    if arr[i][1] == "b":
        count += 1
    elif arr[i][1] == "e":
        count -= 1
    else:
        ans[arr[i][0]] = count

out = []
for i in range(p):
    out.append(ans[d[i]])

open("output.txt", 'w').write(" ".join(map(str, out)))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
