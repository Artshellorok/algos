import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

n, a = map(float, lines[0].split())
n = int(n)

girlande = [float(-1)] * n
girlande[0] = a

l = a
r = 0

while l - r > 0.0000000001:
    girlande[1] = (l+r) / 2
    check = True

    for i in range(2, n):
        girlande[i] = 2 * girlande[i-1] - girlande[i-2] + 2
        if girlande[i] < 0:
            check = False
            break
    if check:
        l = girlande[1]
    else:
        r = girlande[1]

out.write("{:.2f}".format(girlande[n-1]))
print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
