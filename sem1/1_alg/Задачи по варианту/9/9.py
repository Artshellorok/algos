import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
out = open("output.txt", 'w')

n = int(lines[0].rstrip())
a = list(map(int,lines[1].rstrip()))
b = list(map(int,lines[2].rstrip()))
c = [0] * (n+1)
mem = False
for i in range(n-1, -1,-1):
    num = a[i] + b[i]
    if mem: 
        num += 1 
    mem = False
    match num:
        case 0:
            c[i+1] = 0
        case 1:
            c[i+1] = 1
        case _:
            mem = True
            c[i+1] = 0
if mem:
    c[0] = 1
    out.write("".join(map(str,c)))
else:
    out.write("".join(map(str,c[1:])))

print("Время выполнения: " + str(time.perf_counter() -t_start) + " секунд")
print("Использование памяти: " + str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
