import random
import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()


def partition(l, r):
    pivot = a[l]
    j = l
    c = r
    i = l + 1
    while i <= c:
        if a[i] < pivot:
            j += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] > pivot:
            a[c], a[i] = a[i], a[c]
            i -= 1
            c -= 1
        i += 1

    a[l], a[j] = a[j], a[l]
    return j, c


def quickSort(l, r):
    if l < r:
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        m, c = partition(l, r)
        quickSort(l, m-1)
        quickSort(c+1, r)


n = int(lines[0])
a = list(map(int, lines[1].split()))
quickSort(0, len(a)-1)

open("output.txt", 'w').write(" ".join(map(str, a)))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
