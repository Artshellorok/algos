from math import inf
import copy
import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")


def poor_student(n):
    matrix = [[0 for j in range(n + 1)] for i in range(n + 1)]
    mem = [[[0, 0, []] for j in range(n + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        matrix[0][i] = inf
    for i in range(1, n + 1):
        if matrix[i - 1][1] > matrix[i - 1][0] + prices[i] and (
            matrix[i - 1][1] == inf or prices[i] <= 100
        ):
            matrix[i][0] = matrix[i - 1][0] + prices[i]
            mem[i][0] = copy.deepcopy(mem[i-1][0])
            if prices[i] > 100:
                mem[i][0][0] += 1
        else:
            matrix[i][0] = matrix[i - 1][1]
            mem[i][0] = copy.deepcopy(mem[i-1][1])
            mem[i][0][1] += 1
            mem[i][0][2].append(i)
        for j in range(1, n):
            if prices[i] <= 100:
                price1 = matrix[i-1][j] + prices[i]
                price2 = matrix[i-1][j+1]
                if price1 < price2:
                    matrix[i][j] = price1
                    mem[i][j] = copy.deepcopy(mem[i-1][j])
                else:
                    matrix[i][j] = price2
                    mem[i][j] = copy.deepcopy(mem[i-1][j+1])
            else:
                price1 = matrix[i-1][j-1] + prices[i]
                price2 = matrix[i-1][j+1]
                if price1 < price2:
                    matrix[i][j] = price1
                    mem[i][j] = copy.deepcopy(mem[i-1][j-1])
                    mem[i][j][0] += 1
                else:
                    matrix[i][j] = price2
                    mem[i][j] = copy.deepcopy(mem[i-1][j+1])
                    mem[i][j][1] += 1
                    mem[i][j][2].append(i)
    out.write(str(matrix[n][0]))
    out.write("\n" + str(mem[n][0][0] - mem[n]
              [0][1]) + " " + str(mem[n][0][1]))


n = int(lines[0])
prices = [0]
for i in range(n):
    prices.append(int(lines[i+1]))
poor_student(n)

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
