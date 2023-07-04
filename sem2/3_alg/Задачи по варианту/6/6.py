import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

a = lines[0].rstrip()
n = len(a)
z = [0] * n
l = 0
r = 0
for i in range(1, n):
    if i <= r:
        z[i] = min(r-i+1, z[i-l])
    while i+z[i] < n and a[z[i]] == a[i+z[i]]:
        z[i] += 1
    if i + z[i] - 1 > r:
        l = i
        r = i+z[i]-1
out.write(" ".join(map(str, z[1:])))
print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
