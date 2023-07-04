import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()

n = int(lines[0])
a = []
for i in range(1, n+1):
    a.append(i)
for i in range(2, n):
    a[i], a[i//2] = a[i//2], a[i]

open("output.txt", 'w').write(" ".join(map(str, a)))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
