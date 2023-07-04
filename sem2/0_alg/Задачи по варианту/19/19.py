from math import inf
import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
output = open("output.txt", "w")


n = int(lines[0]) + 1
groesse = [0] * n
dp = [[inf for j in range(n)] for i in range(n)]
ant = [[0 for j in range(n)] for i in range(n)]


def calc(l, r):
    if dp[l][r] == inf:
        for i in range(l, r):
            curr = calc(l, i) + calc(i+1, r) + \
                (groesse[l-1] * groesse[i] * groesse[r])
            if curr < dp[l][r]:
                dp[l][r] = curr
                ant[l][r] = i

    return dp[l][r]


def antBauen(l, r):
    if l == r:
        return 'A'

    return '(' + antBauen(l, ant[l][r]) + antBauen(ant[l][r] + 1, r) + ')'


for i in range(1, n):
    groesse[i - 1], groesse[i] = list(map(int, lines[i].split()))
    if dp[i][i]:
        dp[i][i] = 0

calc(1, n-1)
output.write(str(antBauen(1, n-1)))
print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
