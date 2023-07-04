import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
out = open("output.txt", 'w')

n = int(lines[0])
a = list(enumerate(map(float,lines[1].split())))

def quick_sort(l,r):
    i = l
    j = r
    pivot = a[(i+j)//2][1]
    while i <= j:
        while a[i][1] < pivot:
            i+=1
        while a[j][1] > pivot:
            j-=1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if j > l:
        quick_sort(l, j)
    if i < r:
        quick_sort(i, r)

quick_sort(0,n-1)

out.write(f"{a[0][0]+1} {a[n//2][0]+1} {a[n-1][0]+1}")

print("Время выполнения: " + str(time.perf_counter() -t_start) + " секунд")
print("Использование памяти: " + str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
