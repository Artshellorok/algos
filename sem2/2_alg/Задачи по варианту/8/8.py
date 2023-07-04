import queue
import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")


def dijkstra(zu):
    while not q.empty():
        w, v = q.get()
        visited[v] = True
        if v == zu:
            return w
        for i in range(len(adj_matrix[v])):
            if i != v and adj_matrix[v][i] != -1:
                el = adj_matrix[v][i]
                if not visited[i]:
                    q.put((w+el, i))
        return dijkstra(zu)
    return -1


n, m = map(int, lines[0].split())
visited = [False] * n
adj_matrix = [[-1 for j in range(n)] for i in range(n)]
q = queue.PriorityQueue(maxsize=0)

for i in range(m):
    u, v, w = map(int, lines[i+1].split())
    u -= 1
    v -= 1
    adj_matrix[u][v] = w

von, zu = map(int, lines[m+1].split())

q.put((0, von-1))
visited[von-1] = True
out.write(str(dijkstra(zu-1)))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
