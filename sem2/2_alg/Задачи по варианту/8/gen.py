import random
n = 10 ** 4
m = 10 ** 4-1
print(n, m)
for i in range(m):
    print(i+1, i+2, random.randint(0, 10**8))
print(random.randint(1, n), random.randint(1, n))
