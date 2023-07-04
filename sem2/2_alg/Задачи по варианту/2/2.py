import time
import tracemalloc
import sys
sys.setrecursionlimit(1500)
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")


def dfs(v):
    if not visited[v]:
        visited[v] = True
        for i in range(len(adj_list[v])):
            el = adj_list[v][i]
            if not visited[el]:
                dfs(el)


n, m = map(int, lines[0].split())
adj_list = [[] for i in range(n)]
visited = [False] * n
count = 0

for i in range(m):
    a, b = map(int, lines[i+1].split())
    a -= 1
    b -= 1
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(n):
    if not visited[i]:
        count += 1
        dfs(i)
out.write(str(count))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
