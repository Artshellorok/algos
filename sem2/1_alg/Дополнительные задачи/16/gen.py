import random
n = 10000
print(n)
size = 0
i = 0
while i < n:
    typ = random.randint(0, 2)
    if typ == 0:
        size += 1
        print("+1", random.randint(-10**2, 10**2))
        i += 1
    elif typ == 1:
        if size > 0:
            size -= 1
            print("-1", random.randint(-10**2, 10**2))
            i += 1
    elif typ == 2:
        if size > 0:
            x = random.randint(1, size)
            print("0", x)
            i += 1
