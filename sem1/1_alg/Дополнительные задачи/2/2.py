import time
import tracemalloc
lol = "1 "
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
def insertion_sort():
    global lol
    for i in range(1,len(a)):
        j = i
        while a[j-1] > a[j] and j != 0:
            a[j-1], a[j] = a[j], a[j-1]
            j -= 1
        lol += str(j+1) + " "
n = int(lines[0])
a = list(map(int,lines[1].split()))
insertion_sort()
open("output.txt", 'w').write(lol + " ".join(map(str,a)))

print("Время выполнения: " + str(time.perf_counter() -t_start) + " секунд")
print("Использование памяти: " + str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()

