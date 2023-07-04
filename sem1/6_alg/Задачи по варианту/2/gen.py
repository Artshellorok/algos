import random
n = 10**5
print(n)
letters = "abcdefghijklmnopqrstuvwxyz"
for i in range(n):
    phone = random.randint(1, 9999999)
    act = random.randint(1, 3)
    if act == 1:
        word = ""
        for j in range(random.randint(1, 19)):
            word += letters[random.randint(0, 25)]
        print(f"add {phone} {word}")
    elif act == 2:
        print(f"del {phone}")
    else:
        print(f"find {phone}")
