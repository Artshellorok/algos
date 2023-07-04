import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")


def ans(l, r):
    if best[l][r] == -1:
        res[l] = res[r] = ''
    if l == r:
        return
    if best[l][r] == -2:
        if l + 1 == r:
            return
        ans(l+1, r-1)
    else:
        ans(l, best[l][r])
        ans(best[l][r] + 1, r)
    return


inf = 10 ** 9
s = lines[0].strip()
n = len(s)
dp = [[inf] * (n+1) for i in range(n+1)]
best = [[-1] * (n+1) for i in range(n+1)]
for i in range(n+1):
    dp[i][i] = 1
for i in range(n-1):
    if (s[i] == '(' and s[i+1] == ')') or (s[i] == '[' and s[i+1] == ']') or (s[i] == '{' and s[i+1] == '}'):
        dp[i][i+1] = 0
        best[i][i+1] = -2
for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1
        if (s[l] == '(' and s[r] == ')') or (s[l] == '[' and s[r] == ']') or (s[l] == '{' and s[r] == '}'):
            if dp[l][r] > dp[l+1][r-1]:
                dp[l][r] = dp[l+1][r-1]
                best[l][r] = -2
        for m in range(l, r):
            curr = dp[l][m] = dp[m+1][r]
            if dp[l][r] > curr:
                dp[l][r] = curr
                best[l][r] = m
res = list(s)
ans(0, n-1)
out.write(''.join(res))
print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
