import random
n = 100
print(n)
for i in range(100):
    unixtime = i * 10 + random.randint(1, 10)
    print(unixtime//60, unixtime % 60, random.randint(0, 100))
