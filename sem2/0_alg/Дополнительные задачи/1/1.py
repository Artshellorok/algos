import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

n, w = map(int, lines[0].split())

sachen = []
for i in range(n):
    preis, gewicht = map(int, lines[i+1].split())
    preis_pro_gewicht = preis / gewicht
    sachen.append([gewicht, preis_pro_gewicht])
sachen = sorted(sachen, key=lambda x: x[1], reverse=True)
antwort = 0
for gewicht, ppg in sachen:
    minusgewicht = min(gewicht, w)
    w -= minusgewicht
    antwort += minusgewicht * ppg
    if w == 0:
        break
out.write("{0:.4f}".format(antwort))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
