import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

n = int(lines[0])
nums = list(map(int, lines[1].split()))

s = sum(nums) // 2
output = []

if sum(nums) % 2 != 0:
    out.write(str(-1))
else:
    dp = [[0 for i in range(s+1)] for y in range(n)]
    for i in range(n):
        dp[i][0] = 1
    dp[0][nums[0]] = 1
    for i in range(1, n):
        for j in range(1, s+1):
            dp[i][j] = dp[i-1][j]
            if nums[i] <= j:
                dp[i][j] = max(dp[i][j], dp[i-1][j-nums[i]])
    if dp[n-1][s] != 1:
        out.write(str(-1))
    else:
        i = n-1
        j = s
        while j != 0 and i > 0:
            if dp[i-1][j-nums[i]] == 0:
                i -= 1
            else:
                output.append(nums[i])
                j -= nums[i]
                i -= 1
        if j != 0:
            output.append(nums[0])

        output.reverse()
        out.write(" ".join(map(str, output)))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
