import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
out = open("output.txt", 'w')
n = int(lines[0].rstrip())
let = lines[1].rstrip()
occur = {}
for letter in let:
    if letter not in occur:
        occur[letter] = 1
    else:
        occur[letter] += 1
occur = dict(sorted(occur.items()))
nummer = ""
again = ""
for key in occur:
    if occur[key] % 2 == 1 and nummer == "":
        nummer = key
    num = occur[key] // 2
    if num:
        again += key * num
out.write(again + nummer + again[::-1])



print("Время выполнения: " + str(time.perf_counter() -t_start) + " секунд")
print("Использование памяти: " + str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
