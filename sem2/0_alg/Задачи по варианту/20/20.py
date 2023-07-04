import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
output = open("output.txt", "w")


n, k = map(int, lines[0].split())
dp = [[-1 for i in range(n)] for j in range(2)]
s = lines[1]
count = 1
for i in range(n-1):
    if s[i] == s[i+1]:
        dp[1][i] = 0
        count += 1
    else:
        dp[1][i] = 1
        if 1 <= k:
            count += 1
    dp[0][i] = 0
    count += 1
dp[0][n-1] = 0
for L in range(3, n+1):
    dp_new = [-1 for i in range(n)]
    for i in range(n-L+1):
        j = i + L - 1
        index = (L-1) % 2
        if s[i] != s[j]:
            dp_new[i] = dp[index][i+1] + 1
        else:
            dp_new[i] = dp[index][i+1]
        if dp_new[i] <= k:
            count += 1
    dp[index % 2] = dp_new
output.write(str(count))
print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
