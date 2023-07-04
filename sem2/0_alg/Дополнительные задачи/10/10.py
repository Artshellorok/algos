import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

n, s = map(int, lines[0].split())
aepfel = []

for i in range(n):
    verloren, bekommen = map(int, lines[i+1].split())
    aepfel.append([i, verloren, bekommen])
aepfel = sorted(aepfel, key=lambda x: x[2] - x[1], reverse=True)

count = 0
curr = s
fehler = False
ans = []
hist = [False] * n

while count < n:
    gefunden = False
    for i in range(n):
        apfel = aepfel[i]
        if (curr > apfel[1]) and (not hist[apfel[0]]):
            count += 1
            gefunden = True
            curr += (bekommen - verloren)
            if curr < 0:
                out.write(str(-1))
                fehler = True
            hist[apfel[0]] = True
            ans.append(apfel[0] + 1)
            break
    if not gefunden:
        fehler = True
        out.write(str(-1))
        break
    if fehler:
        break
if not fehler:
    out.write(" ".join(map(str, ans)))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
