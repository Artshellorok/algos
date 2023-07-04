import random

for i in range(300000):
    typ = random.randint(0, 1)
    if typ:
        print(">", random.randint(1, 10**9))
    else:
        print("+", random.randint(1, 10**9))
print()
