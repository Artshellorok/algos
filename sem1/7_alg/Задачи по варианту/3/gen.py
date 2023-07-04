import random

alph = "abcdefghijklmnopqrstuvwxyz"
n = 900
str1 = ""
str2 = ""
for i in range(n):
    str1 += alph[random.randint(0, 25)]
    str2 += alph[random.randint(0, 25)]
print(str1)
print(str2)
