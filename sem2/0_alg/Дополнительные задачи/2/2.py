import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

d = int(lines[0])
m = int(lines[1])
n = int(lines[2])
stops = list(map(int, lines[3].split()))
effective_spot = 0
count = 0
last = 0
for i in range(n):
    stop = stops[i]
    if stop - effective_spot <= m:
        last = stop
    else:
        count += 1
        effective_spot = last
if d - effective_spot <= m:
    out.write(str(count))
else:
    if d - last <= m:
        out.write(str(count+1))
    else:
        out.write("-1")

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
