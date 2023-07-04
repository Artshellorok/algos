import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
output = open("output.txt", "w")

n = int(lines[0])
wohner = []
for i in range(n):
    start, end = map(int, lines[i+1].split())
    wohner.append([start, end])
wohner = sorted(wohner, key=lambda x: x[0])
minstart = None
minend = None
out = []
count = 0
for start, end in wohner:
    if minstart == None:
        minstart = start
        minend = end
    else:
        if start > minend:
            out.append(minend)
            minstart = start
            minend = end
            count += 1
        else:
            minend = min(minend, end)
            minstart = max(minstart, start)

output.write(str(count+1) + "\n")
output.write(" ".join(map(str, out + [minend])))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
