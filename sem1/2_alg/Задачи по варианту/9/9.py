from copy import copy, deepcopy
from math import log, ceil
import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()


def split(a):
    row = len(a) // 2
    col = len(a[0]) // 2
    m1 = []
    for i in range(row):
        m1.append([])
        for j in range(col):
            m1[i].append(a[i][j])
    m2 = []
    for i in range(row):
        m2.append([])
        for j in range(col, len(a[0])):
            m2[i].append(a[i][j])
    m3 = []
    for i in range(row, len(a)):
        m3.append([])
        for j in range(col):
            m3[i-row].append(a[i][j])
    m4 = []
    for i in range(row, len(a)):
        m4.append([])
        for j in range(col, len(a[0])):
            m4[i-row].append(a[i][j])
    return m1, m2, m3, m4


def minus(x, y):
    z = deepcopy(x)
    for i in range(len(x)):
        for j in range(len(x)):
            z[i][j] -= y[i][j]
    return z


def plus(x, y):
    z = deepcopy(x)
    for i in range(len(x)):
        for j in range(len(x)):
            z[i][j] += y[i][j]
    return z


def strassen(x, y):
    if len(x) == 1:
        return [[x[0][0]*y[0][0]]]
    a, b, c, d = split(x)
    e, f, g, h = split(y)
    p1 = strassen(a, minus(f, h))
    p2 = strassen(plus(a, b), h)
    p3 = strassen(plus(c, d), e)
    p4 = strassen(d, minus(g, e))
    p5 = strassen(plus(a, d), plus(e, h))
    p6 = strassen(minus(b, d), plus(g, h))
    p7 = strassen(minus(a, c), plus(e, f))
    step1 = plus(p5, p4)
    step2 = minus(step1, p2)
    step3 = plus(step2, p6)
    c11 = step3
    c12 = plus(p1, p2)
    c21 = plus(p3, p4)
    c22 = minus(minus(plus(p1, p5), p3), p7)
    rows = []
    for i in range(len(c11)):
        rows.append(c11[i] + c12[i])
    for i in range(len(c21)):
        rows.append(c21[i] + c22[i])
    return rows


n1 = int(lines[0])

a = []
b = []
n = 2**ceil(log(n1, 2))
for i in range(n1):
    a.append(list(map(int, lines[i+1].split())))
    a[i] += [0] * (n - n1)
for i in range(n1):
    b.append(list(map(int, lines[n1+i+1].split())))
    b[i] += [0] * (n - n1)
for i in range(n - n1):
    a.append([0]*n)
    b.append([0]*n)
out = strassen(a, b)
output = ""
for i in range(n1):
    for j in range(n1):
        output += str(out[i][j]) + ' '
    output += '\n'  # That's a \n

open("output.txt", 'w').write(output)

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
