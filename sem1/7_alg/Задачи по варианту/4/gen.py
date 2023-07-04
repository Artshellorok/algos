import random
n = 100
m = 100
str1 = ""
str2 = ""
print(n)
for i in range(n):
    str1 += str(random.randint(-10**9, 10**9)) + " "
print(str1)
print(m)
for i in range(m):
    str2 += str(random.randint(-10**9, 10**9)) + " "
print(str2)
