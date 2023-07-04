import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

k, n = map(int, lines[0].split())
stiefeln = sorted(list(map(int, lines[1].split())))
summ = 0
count = 0
for i in range(n):
    if summ + stiefeln[i] <= k:
        summ += stiefeln[i]
        count += 1
    else:
        break
out.write(str(count))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
