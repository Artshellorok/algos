import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
a,b = map(int,open("input.txt", "r").readline().rstrip().split())
open("output.txt", 'w').write(str(a+b))
print("Время выполнения: " + str(time.perf_counter() -t_start) + " секунд")
print("Использование памяти: " + str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
