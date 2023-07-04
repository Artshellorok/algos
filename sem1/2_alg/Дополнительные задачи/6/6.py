import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
wr = open("output.txt", 'w')


def maxSubArray(l, r):
    if r - l <= 1:
        return (l, r, a[l])

    pivot = (l + r) // 2

    ll, lr, lsum = maxSubArray(l, pivot)
    rl, rr, rsum = maxSubArray(pivot, r)
    xl, xr, xsum = maxCrossingSum(l, pivot, r)

    if lsum >= rsum and lsum >= xsum:
        return (ll, lr, lsum)
    elif rsum >= lsum and rsum >= xsum:
        return (rl, rr, rsum)
    else:
        return (xl, xr, xsum)


def maxCrossingSum(l, pivot, r):
    lsum = -9999999
    sum = 0
    for i in range(pivot-1, l-1, -1):
        sum += a[i]
        if sum > lsum:
            lsum = sum
            maxl = i
    rsum = -9999999
    sum = 0
    for i in range(pivot, r):
        sum += a[i]
        if sum > rsum:
            rsum = sum
            maxr = i
    return (maxl, maxr, lsum+rsum)


n = int(lines[0])
arr = list(map(int, lines[1].split()))
a = []
for i in range(1, n):
    a.append(arr[i] - arr[i-1])
data = maxSubArray(0, n-1)
if data[0]:
    wr.write(
        f"BUY on day {data[0]+1}\nSELL on day {data[1]+1}\nPROFIT:  {data[2]}")
else:
    wr.write(
        f"BUY on day {data[0]+1}\nSELL on day {data[1]+2}\nPROFIT:  {data[2]}")

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
