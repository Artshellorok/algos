import random
n = 10**6
minuses = 0
pluses = 0
print(n)
for i in range(n):
    plus = random.randint(0, 1)
    if plus or minuses == pluses:
        pluses += 1
        num = random.randint(1, 10**9)
        print(f"+ {num}")
    else:
        minuses += 1
        print("-")
