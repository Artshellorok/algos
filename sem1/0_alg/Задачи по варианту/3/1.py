import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
f1 = 0
f2 = 1
n = int(open("input.txt", "r").readline().rstrip())
for i in range(2, n+1):
    f3 = (f2 + f1) % 10
    f1 = f2
    f2 = f3
if n != 0:
    open("output.txt", "w").write(str(f2))
else:
    open("output.txt", "w").write("0")

print("Время выполнения: " + str(time.perf_counter() -t_start) + " секунд")
print("Использование памяти: " + str(tracemalloc.get_traced_memory()[1]) + " байт")

tracemalloc.stop()
