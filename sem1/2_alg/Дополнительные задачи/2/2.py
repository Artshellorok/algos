import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
wr = open("output.txt", 'w')


def merge(x, y, l, r):
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
    wr.write(f'{l+1} {r} {result[0]} {result[-1]}' + '\n')
    return result


def mergeSort(arr, l, r):
    if len(arr) >= 2:
        pivot = len(arr)//2
        piv = (l+r) // 2
        arr1 = mergeSort(arr[:pivot], l, piv)
        arr2 = mergeSort(arr[pivot:], piv, r)
        return merge(arr1, arr2, l, r)
    else:
        return arr


n = int(lines[0])
arr = list(map(int, lines[1].split()))
arr = mergeSort(arr, 0, n)

wr.write(" ".join(map(str, arr)))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
