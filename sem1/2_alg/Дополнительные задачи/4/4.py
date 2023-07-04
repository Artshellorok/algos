import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
wr = open("output.txt", 'w')


def binSearch(el):
    l = 0
    r = n-1
    while l <= r:
        pivot = (l + r) // 2
        pivot_el = a[pivot]
        if pivot_el == el:
            return pivot
        elif pivot_el < el:
            l = pivot+1
        else:
            r = pivot-1
    return -1


n = int(lines[0])
a = list(map(int, lines[1].split()))
m = int(lines[2])
els = list(map(int, lines[3].split()))
output = ""
for el in els:
    output += str(binSearch(el)) + ' '
wr.write(output)
print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
