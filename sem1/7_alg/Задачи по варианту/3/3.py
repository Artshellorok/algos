import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

a = lines[0]
b = lines[1]

n, m = len(a), len(b)
if n > m:
    a, b = b, a
    n, m = m, n

curr_row = []
for i in range(n+1):
    curr_row.append(i)

for i in range(1, m + 1):
    prev_row, curr_row = curr_row, [i] + [0] * n
    for j in range(1, n + 1):
        move_aus_a = prev_row[j] + 1
        move_aus_b = curr_row[j-1] + 1
        fortsetzen = prev_row[j-1]
        if a[j-1] != b[i-1]:
            fortsetzen += 1
        curr_row[j] = min(move_aus_a, move_aus_b, fortsetzen)

out.write(str(curr_row[n]))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
