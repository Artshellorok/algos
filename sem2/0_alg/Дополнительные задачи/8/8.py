import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

n = int(lines[0])
vorlesungen = []
for i in range(n):
    start, end = map(int, lines[i+1].split())
    vorlesungen.append([start, end])
vorlesungen = sorted(vorlesungen, key=lambda x: x[1])
persist_end = 0
count = 0
for start, end in vorlesungen:
    if start >= persist_end:
        count += 1
        persist_end = end
out.write(str(count))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
