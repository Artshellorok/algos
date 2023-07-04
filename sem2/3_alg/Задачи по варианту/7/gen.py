import random

alph = "abcdefghijklmnopqrstuvwxyz"
s = 0

while s < 10**5:
    n = random.randint(1, 100)
    m = random.randint(1, 100)
    s1 = ""
    s2 = ""
    for i in range(n):
        s1 = s1 + alph[random.randint(0, 25)]
    for i in range(m):
        s2 = s2 + alph[random.randint(0, 25)]
    print(s1, s2)
    s += n
    s += m
