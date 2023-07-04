import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()

n = int(lines[0])
a = list(map(int, lines[1].split()))
curr = [-1, -1, -999999999]
maxi = [-1, -1, -999999999]
for i in range(n):
    if curr[2] > 0:
        curr[1] = i
        curr[2] += a[i]
    else:
        curr[0] = i
        curr[1] = i+1
        curr[2] = a[i]
    if curr[2] > maxi[2]:
        maxi = curr[:]
arr = a[maxi[0]:maxi[1]+1]
open("output.txt", 'w').write(" ".join(map(str, arr)))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
