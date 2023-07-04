import random
n = 1000
print(n)
for i in range(n):
    start = random.randint(1, 1440)
    print(start, random.randint(start, 1440))
