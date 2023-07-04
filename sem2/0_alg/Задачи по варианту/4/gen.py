import random
n = 100
print(n)
for i in range(n):
    start = random.randint(0, 10**9)
    end = random.randint(start, 10**9)
    print(start, end)
