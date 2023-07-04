from random import randint
n = 10**5//2
print(n)
minuses = 0
pluses = 0
for i in range(n):
    plus = randint(0, 2)
    if plus == 1 or minuses == pluses:
        pluses += 1
        num = randint(1, 10**9)
        print(f"+ {num}")
    elif plus == 2:
        print("?")
    else:
        minuses += 1
        print("-")
