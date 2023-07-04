import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
out = open("output.txt", 'w')


def median(first, second, third):
    if first[0] <= second[0] <= third[0]:
        return second
    elif first[0] <= third[0] <= second[0]:
        return third
    elif second[0] <= first[0] <= third[0]:
        return first
    elif second[0] <= third[0] <= first[0]:
        return third
    elif third[0] <= first[0] <= second[0]:
        return first
    elif third[0] <= second[0] <= first[0]:
        return second


def quickSort(l, r):
    i = l
    j = r
    pivot = median([a[l], l], [a[(l+r) // 2], (i+j) // 2], [a[r], r])
    while i <= j:
        while a[i] < pivot[0]:
            i += 1
        while a[j] > pivot[0]:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if j > l:
        quickSort(l, j)
    if i < r:
        quickSort(i, r)


n = int(lines[0])
a = []
a = list(map(int, lines[1].split()))
quickSort(0, n-1)
out.write(" ".join(list(map(str, a))))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
