import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
out = open("output.txt", 'w')
if len(lines) < 2:
    out.write("-1")
else:
    nums = list(map(int,lines[0].split()))
    if len(nums) == 0:
        out.write("-1")
    else:
        v = int(lines[1])
        occurences = { 'count' :0, 'arr': []}

        for i in range(len(nums)):
            if v == nums[i]:
                occurences['count'] += 1
                occurences['arr'].append(i)
        if occurences['count'] == 0:
            out.write("-1") 
        elif occurences['count'] == 1:
            out.write(str(occurences['arr'][0]))
        else:
            out.write(str(occurences['count']) + '\n')
            out.write(",".join(map(str,occurences['arr'])))
print("Время выполнения: " + str(time.perf_counter() -t_start) + " секунд")
print("Использование памяти: " + str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
