import sys
import queue
import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")


def dijkstra():
    while not q.empty():
        w, v = q.get()
        visited[v] = True
        for i in range(len(adj_matrix[v])):
            el = adj_matrix[v][i]
            if el != -1:
                if not visited[i]:
                    new_cost = w + el
                    if new_cost < dist[i]:
                        q.put((new_cost, i))
                        dist[i] = new_cost


m = int(lines[0])
sootv = {}
n = 0
q = queue.PriorityQueue(maxsize=0)
inputs = []
for i in range(m):
    von, d_, zu = lines[i+1].split()
    inputs.append([von, d_, zu])
    if von not in sootv:
        sootv[von] = n
        n += 1
    if zu not in sootv:
        sootv[zu] = n
        n += 1

visited = [False] * n
INT_MAX = 9999999999999999999
dist = [INT_MAX] * n
adj_matrix = [[-1 for j in range(n)] for i in range(n)]

for i in range(m):
    von, d_, zu = inputs[i]
    von = sootv[von]
    zu = sootv[zu]
    adj_matrix[von][zu] = 1

von = lines[m+1].rstrip()
zu = lines[m+2].rstrip()
if von == zu:
    out.write("0")
else:
    if von not in sootv or zu not in sootv:
        out.write("-1")
    else:
        von = sootv[von]
        zu = sootv[zu]

        q.put((0, von))
        visited[von] = True
        dist[von] = 0
        dijkstra()
        if dist[zu] == INT_MAX:
            out.write("-1")
        else:
            out.write(str(dist[zu]))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
