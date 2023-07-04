from random import randint
n = 35
m = 4
alph = "SCDH"
alph2 = "6789TJQKA"
print(n, m, alph[randint(0, 3)])
for i in range(n):
    karte = alph2[randint(0, 8)] + alph[randint(0, 3)]
    print(karte, end=' ')
print()
for i in range(m):
    karte = alph2[randint(0, 8)] + alph[randint(0, 3)]
    print(karte, end=' ')
