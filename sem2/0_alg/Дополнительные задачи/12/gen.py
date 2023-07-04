import random
n = 40000
print(n)
for i in range(n):
    print(random.randint(1, i+1), end=' ')
