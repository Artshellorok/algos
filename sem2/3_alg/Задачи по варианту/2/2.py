import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

a = lines[0].replace(" ", "")

count = 0

for i in range(len(a) - 2):
    for j in range(i+2, len(a)):
        if a[i] == a[j]:
            count += j - i - 1
out.write(str(count))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
