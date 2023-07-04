import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()


def quick_sort(l, r):
    i = l
    j = r
    pivot = citations[(i+j)//2]
    while i <= j:
        while citations[i] < pivot:
            i += 1
        while citations[j] > pivot:
            j -= 1
        if i <= j:
            citations[i], citations[j] = citations[j], citations[i]
            i += 1
            j -= 1
    if j > l:
        quick_sort(l, j)
    if i < r:
        quick_sort(i, r)


citations = list(map(int, lines[0].split(",")))
n = len(citations)
quick_sort(0, n-1)

for i in range(n):
    h = citations[i]
    if n-i <= h:
        open("output.txt", 'w').write(str(n-i))
        print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
        print("Использование памяти: " +
              str(tracemalloc.get_traced_memory()[1]) + " байт")
        tracemalloc.stop()
        exit()
open("output.txt", "w").write("0")
print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
