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
def selection_sort():
    for i in range(n-1):
        mini = a[i]
        min_index = i
        for j in range(i+1,n):
            if a[j] < mini:
                mini = a[j]
                min_index = j
        swap(i, min_index)

        

n = int(lines[0])
a = list(map(int,lines[1].split()))
selection_sort()

open("output.txt", 'w').write(" ".join(map(str,a)))

print("Время выполнения: " + str(time.perf_counter() -t_start) + " секунд")
print("Использование памяти: " + str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
