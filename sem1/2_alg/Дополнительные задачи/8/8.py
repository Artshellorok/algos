from math import log, ceil
import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
wr = open("output.txt", 'w')


def summ(a, b):
    if len(a) > len(b):
        diff = len(a) - len(b)
        for i in range(len(b)):
            a[diff+i] += b[i]
        return a
    else:
        diff = len(b) - len(a)
        for i in range(len(a)):
            b[diff+i] += a[i]
        return b


def minus(a, b):
    if len(a) > len(b):
        diff = len(a) - len(b)
        for i in range(len(b)):
            a[diff+i] -= b[i]
        return a
    else:
        diff = len(b) - len(a)
        for i in range(len(b)):
            b[i] *= -1
        for i in range(len(a)):
            b[diff+i] += a[i]
        return b


def multiplybyx(a, x, n):
    c = [0] * (2*n)
    for i in range(n):
        c[i+x] = a[i]
    return c


def multiply(a, b, n):
    if n <= 2:
        c = [0] * (2*n)
        for i in range(n):
            for j in range(n):
                c[1+i+j] += a[i] * b[j]
        return c
    pivot = n // 2
    a1 = a[:pivot]
    a0 = a[pivot:]
    b1 = b[:pivot]
    b0 = b[pivot:]

    a1b1 = multiply(a1, b1, n // 2)
    a0b0 = multiply(a0, b0, n // 2)

    step1 = summ(a0, a1)
    step2 = summ(b0, b1)
    step3 = multiply(step1, step2, n//2)
    step4 = minus(step3, a0b0[:])
    step5 = minus(step4, a1b1[:])
    third = step5

    step1 = multiplybyx(a1b1, 0, n)
    step2 = multiplybyx(third, n-n//2, n)
    step3 = summ(step1, step2)
    step4 = summ(step3, a0b0)
    c = step4
    return c


n1 = int(lines[0])
a1 = list(map(int, lines[1].split()))
b1 = list(map(int, lines[2].split()))
n = 2**ceil(log(n1, 2))
a = []
b = []
for i in range(n - n1):
    a.append(0)
    b.append(0)
a = a + a1
b = b + b1
out = multiply(a, b, n)
wr.write(" ".join(map(str, out)))
print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
