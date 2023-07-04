import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()


def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while a[j-1] > a[j] and j != 0:
            a[j-1], a[j] = a[j], a[j-1]
            j -= 1
    return a


def bucketSort(arr, n):
    b = []
    for i in range(n):
        b.append([])
    for i in range(n):
        bi = int(n*arr[i])
        b[bi].append(arr[i])

    for i in range(n):
        b[i] = insertion_sort(b[i])

    index = 0
    arr.clear()
    for i in range(n):
        for j in range(len(b[i])):
            arr.append(b[i][j])


def sortMerge(arr, n):
    minus = []
    plus = []

    for i in range(n):
        if arr[i] < 0:
            minus.append(-1*arr[i])
        else:
            plus.append(arr[i])

    bucketSort(minus, len(minus))
    bucketSort(plus, len(plus))

    for i in range(len(minus)):
        arr[i] = -1*minus[len(minus)-1-i]

    for i in range(len(minus), n):
        arr[i] = plus[i-len(minus)]


n = int(lines[0])
arr = list(map(float, lines[1].split()))
sortMerge(arr, n)

open("output.txt", 'w').write(" ".join(map(str, arr)))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
