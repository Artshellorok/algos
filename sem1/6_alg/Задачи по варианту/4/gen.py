import random
n = 2*10**5
print(n)
letters = "abcdefghijklmnopqrstuvwxyz"
for i in range(n):
    key = ""
    for j in range(random.randint(1, 19)):
        key += letters[random.randint(0, 25)]
    act = random.randint(1, 5)
    if act == 1:
        value = ""
        for j in range(random.randint(1, 19)):
            value += letters[random.randint(0, 25)]
        print(f"put {key} {value}")
    elif act == 2:
        print(f"delete {key}")
    elif act == 3:
        print(f"prev {key}")
    elif act == 4:
        print(f"next {key}")
    else:
        print(f"get {key}")
