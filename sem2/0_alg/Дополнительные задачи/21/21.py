import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")


def karteZuZahl(num):
    wechseln = {
        "6": 0,
        "7": 1,
        "8": 2,
        "9": 3,
        "T": 4,
        "J": 5,
        "Q": 6,
        "K": 7,
        "A": 8
    }
    return wechseln[num]


sortierte_karte = {"S": [], "C": [], "D": [], "H": []}


def greedSort():
    for i in range(len(karte)):
        el = karte[i]
        sortierte_karte[el[1]].append(
            karteZuZahl(el[0])
        )
    sortierte_karte["S"].sort()
    sortierte_karte["C"].sort()
    sortierte_karte["D"].sort()
    sortierte_karte["H"].sort()


n, m, r = lines[0].split()
n = int(n)
m = int(m)
karte = lines[1].split()
greedSort()
schlagen = lines[2].split()
ans = True
for i in range(len(schlagen)):
    el = schlagen[i]
    familie = el[1]
    nummer = karteZuZahl(el[0])
    istSchlagbar = False
    for j in range(len(sortierte_karte[familie])):
        el2 = sortierte_karte[familie][j]
        if el2 > nummer:
            istSchlagbar = True
            sortierte_karte[familie].pop(j)
            break
    if not istSchlagbar and familie != r:
        for j in range(len(sortierte_karte[r])):
            sortierte_karte[r].pop(j)
            istSchlagbar = True
            break
    if not istSchlagbar:
        ans = False
        break
if ans:
    out.write("YES")
else:
    out.write("NO")

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
