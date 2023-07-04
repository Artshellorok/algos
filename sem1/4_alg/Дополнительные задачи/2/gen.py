from random import randint
n = 10**5
print(n)
minuses = 0
pluses = 0
for i in range(n):
    plus = randint(0, 1)
    if plus or minuses == pluses:
        pluses += 1
        num = randint(1, 10**9)
        print(f"+ {num}")
    else:
        minuses += 1
        print("-")
