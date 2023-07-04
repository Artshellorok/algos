import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
wr = open("output.txt", 'w')

inv = 0


def merge(x, y, l, r):
    global inv
    result = []
    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i] > y[j]:
            result.append(y[j])
            j += 1
            inv += len(x) - i
        else:
            result.append(x[i])
            i += 1
    result += x[i:]
    result += y[j:]
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

wr.write(str(inv))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
