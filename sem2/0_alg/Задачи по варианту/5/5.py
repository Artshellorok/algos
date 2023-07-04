import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
output = open("output.txt", "w")

n = int(lines[0])
summ = 0
i = 1
out = []
while summ + i <= n:
    summ += i
    out.append(i)
    i += 1
if summ != n:
    out[len(out)-1] += (n - summ)
output.write(str(len(out)) + "\n")
output.write(" ".join(map(str, out)))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
