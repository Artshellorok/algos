import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()

n = int(lines[0])
a = [-1] + list(map(int, lines[1].split()))
out = open("output.txt", "w")

for i in range(1, n+1):
    if i % 2 == 0:
        parent = a[i//2]
    else:
        parent = a[(i-1)//2]
    if a[i] <= parent:
        out.write("NO")
        print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
        print("Использование памяти: " +
              str(tracemalloc.get_traced_memory()[1]) + " байт")
        tracemalloc.stop()
        exit()

out.write("YES")
print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
