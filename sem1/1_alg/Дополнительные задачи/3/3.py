import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
def swap(i,j):
    d = a[i]
    a[i] = a[j]
    a[j] = d

def insertion_sort():
    for i in range(1,len(a)):
        j = i
        while a[j-1] < a[j] and j != 0:
            swap(j-1,j)
            j -= 1
n = int(lines[0])
a = list(map(int,lines[1].split()))
insertion_sort()
open("output.txt", 'w').write(" ".join(map(str,a)))

print("Время выполнения: " + str(time.perf_counter() -t_start) + " секунд")
print("Использование памяти: " + str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()

