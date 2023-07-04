import random

for i in range(3000):
    typ = random.randint(0, 1)
    if typ:
        print("?", random.randint(1, 10**3))
    else:
        print("+", random.randint(1, 10**3))
