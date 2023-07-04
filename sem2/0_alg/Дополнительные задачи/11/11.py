import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

w, n = map(int, lines[0].split())
gewichte = list(map(int, lines[1].split()))
dp = [[0 for x in range(w+1)] for y in range(n+1)]
for i in range(1, n+1):
    for j in range(1, w+1):
        if j >= gewichte[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1]
                           [j - gewichte[i-1]] + gewichte[i-1])
        else:
            dp[i][j] = dp[i-1][j]
out.write(str(dp[n][w]))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
