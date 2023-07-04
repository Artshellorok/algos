import random
n = 30
print(n)
size = 0
i = 0
while i < n:
    typ = random.randint(0, 3)
    if typ == 0:
        size += 1
        print("+", random.randint(1, 10**3))
        i += 1
    elif typ == 1:
        size -= 1
        print("-", random.randint(1, 10**3))
        i += 1
    elif typ == 2:
        x = random.randint(1, 10**3)
        print("?", x)
        i += 1
    elif typ == 3:
        s1 = random.randint(10**2, 10**3-1)
        s2 = random.randint(s1, 10**3)
        print("s", s1, s2)
