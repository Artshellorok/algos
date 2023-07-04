from random import randint
n = 5000
k = randint(0, n)
alph = "abcdefghijklmnopqrstuvwxyz"
print(k, n)
for i in range(n):
    print(alph[randint(0, 25)], end='')
