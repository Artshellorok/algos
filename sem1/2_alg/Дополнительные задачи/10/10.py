import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()


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
        if arr1[pivot-1] > arr2[0]:
            return merge(arr1, arr2)
    else:
        return arr


n = int(lines[0])
arr = list(map(int, lines[1].split()))
arr = mergeSort(arr)

open("output.txt", 'w').write(" ".join(map(str, arr)))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
