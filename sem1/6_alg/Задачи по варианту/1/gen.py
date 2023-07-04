import random
n = 10**5
print(n)
for i in range(n):
    op = random.randint(1, 3)
    val = random.randint(1, 10**18)
    if op == 1:
        print("A", val)
    elif op == 2:
        print("D", val)
    else:
        print("?", val)
