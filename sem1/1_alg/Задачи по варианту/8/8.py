import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
out = open("output.txt", 'w')

def swap(i,j):
    d = a[i]
    a[i] = a[j]
    a[j] = d
def quick_sort(l,r):
    i = l
    j = r
    pivot = a[(i+j)//2]
    while i <= j:
        while a[i] < pivot:
            i+=1
        while a[j] > pivot:
            j-=1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            out.write(f"Swap elements at indices {i} and {j}. ")
            i += 1
            j -= 1
    if j > l:
        quick_sort(l, j)
    if i < r:
        quick_sort(i, r)

        

n = int(lines[0])
a = list(map(int,lines[1].split()))
quick_sort(0,n-1)

out.write("No more swaps needed")

print("Время выполнения: " + str(time.perf_counter() -t_start) + " секунд")
print("Использование памяти: " + str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
