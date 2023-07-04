import random
import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
f = open("output.txt", 'w')
lines = file.readlines()


def countSort(arr, j):
    global swaps, swaps_d

    n = len(arr)

    output = [""] * n
    count = [0] * 256

    for i in range(n):
        index = arr[i][j]
        count[ord(index)] += 1
    for i in range(ord('a')+1, ord('z')+1):
        count[i] += count[i-1]

    for i in range(n-1, -1, -1):
        index = arr[i][j]
        if count[ord(index)] > 0:
            output[count[ord(index)]-1] = arr[i]
            swaps_d[count[ord(index)]-1] = swaps[i]
            count[ord(index)] -= 1
    swaps = swaps_d[:]

    return output


def radixSort(arr):
    for i in range(m-1, m-k-1, -1):
        arr = countSort(arr, i)


n, m, k = map(int, lines[0].split())
swaps = []
for i in range(1, n+1):
    swaps.append(i)
swaps_d = swaps[:]
strings = ["" for x in range(n)]
for i in range(m):
    string = lines[i+1]
    for j in range(n):
        strings[j] += string[j]
radixSort(strings)
f.write(" ".join(list(map(str, swaps))))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
