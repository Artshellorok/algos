import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

n = int(lines[0])
a = list(map(int, lines[1].split()))
b = list(map(int, lines[2].split()))
negative_a = []
negative_b = []
positive_a = []
positive_b = []
for i in range(n):
    if a[i] <= 0:
        negative_a.append(a[i])
    else:
        positive_a.append(a[i])
    if b[i] <= 0:
        negative_b.append(b[i])
    else:
        positive_b.append(b[i])
negative_a = sorted(negative_a)
negative_b = sorted(negative_b)

summ = 0
if len(negative_b) > len(negative_a):
    for i in range(len(negative_a)):
        summ += negative_a[i] * negative_b[i]
    for i in range(len(negative_a), len(negative_b)):
        positive_b.append(negative_b[i])
else:
    for i in range(len(negative_b)):
        summ += negative_a[i] * negative_b[i]
    for i in range(len(negative_b), len(negative_a)):
        positive_a.append(negative_a[i])

positive_a = sorted(positive_a)
positive_b = sorted(positive_b)
for i in range(len(positive_a)):
    summ += positive_a[i] * positive_b[i]
out.write(str(summ))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
