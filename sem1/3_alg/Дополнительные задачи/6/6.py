import time
import tracemalloc
tracemalloc.start()
file = open('input.txt')
lines = file.readlines()
wr = open("output.txt", 'w')


def merge(x, y):
    result = []
    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i] > y[j]:
            result.append(y[j])
            j += 1
        else:
            result.append(x[i])
            i += 1
    result += x[i:]
    result += y[j:]
    return result


def mergeSort(arr):
    if len(arr) >= 2:
        pivot = len(arr)//2
        arr1 = mergeSort(arr[:pivot])
        arr2 = mergeSort(arr[pivot:])
        return merge(arr1, arr2)
    else:
        return arr


def countSort(arr):
    length = 40001
    a = [0] * (40001)
    for i in range(len(arr)):
        a[arr[i]] += 1
    out = []
    for i in range(40001):
        if a[i]:
            out.append(i)
    return out


def quick_sort(l, r):
    i = l
    j = r
    pivot = c[(i+j)//2]
    while i <= j:
        while c[i] < pivot:
            i += 1
        while c[j] > pivot:
            j -= 1
        if i <= j:
            c[i], c[j] = c[j], c[i]
            i += 1
            j -= 1
    if j > l:
        quick_sort(l, j)
    if i < r:
        quick_sort(i, r)


n, m = map(int, lines[0].split())
a1 = list(map(int, lines[1].split()))
a2 = list(map(int, lines[2].split()))
c = []
for i in range(n):
    for j in range(m):
        c.append(a1[i]*a2[j])
t_start = time.perf_counter()
# c1 = mergeSort(c)
# print("Время выполнения merge sort: " +
#       str(time.perf_counter() - t_start) + " секунд")
t_start = time.perf_counter()
c2 = countSort(c)
print("Время выполнения counting sort: " +
      str(time.perf_counter() - t_start) + " секунд")
# t_start = time.perf_counter()
# quick_sort(0, n*m-1)
# print("Время выполнения quick sort: " +
#       str(time.perf_counter() - t_start) + " секунд")
# print("Использование памяти: " +
#       str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
summ = 0
for i in range(n*m):
    if i % 10 == 0:
        summ += c[i]
wr.write(str(summ))
