import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
output = open("output.txt", "w")

n = int(lines[0])
a = []
for i in range(7):
    cost = int(lines[i+1])
    cost_pro_blatt = cost / (10 ** i)
    a.append({"blaetter": 10**i, "cost": cost,
             "cost_pro_blatt": cost_pro_blatt})
a = sorted(a, key=lambda x: x["cost_pro_blatt"])
cost = 0
mini = 9999999999999999999
n_ = n
for i in range(7):
    order = a[i]
    if order["blaetter"] <= n:
        count = (n // order["blaetter"])
        n -= order["blaetter"] * count
        cost += order["cost"] * count
    if (order["cost"] < mini) and (order["blaetter"] >= n_):
        mini = order["cost"]

output.write(str(min(cost, mini)))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
