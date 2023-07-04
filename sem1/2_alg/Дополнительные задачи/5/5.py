import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
wr = open("output.txt", 'w')


def getMajority(l, r):
    if r - l <= 1:
        return a[l]

    pivot = (l + r) // 2
    l_majority = getMajority(l, pivot)
    r_majority = getMajority(pivot, r)

    if l_majority == r_majority:
        return l_majority

    l_count = countFrequency(l_majority, l, r)
    r_count = countFrequency(r_majority, l, r)

    if l_count > r_count:
        return l_majority
    else:
        return r_majority


def countFrequency(el, l, r):
    count = 0
    for i in range(l, r):
        if a[i] == el:
            count += 1
    return count


n = int(lines[0])
a = list(map(int, lines[1].split()))
num = getMajority(0, n)
if countFrequency(num, 0, n) > n // 2:
    wr.write('1')
else:
    wr.write('0')

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
