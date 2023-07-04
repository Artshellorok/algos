import random
alph = "fa();[]{}"
for i in range(10**5):
    print(alph[random.randint(0, 7)], end='')
