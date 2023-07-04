from random import randint
n = 500
print(n)
alph = "([])"
for i in range(500):
    for i in range(10**3):
        print(alph[randint(0, 3)], end='')
    print()
