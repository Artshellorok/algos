import random
n = 100
mem = {}
for i in range(n):
    act = random.randint(1, 5)
    num = random.randint(-10**9, 10**9)
    if act == 1:
        act_p = "insert"
        mem = {}
    elif act == 2:
        act_p = "exists"
    elif act == 3:
        act_p = "next"
    elif act == 4:
        act_p = "prev"
    else:
        act_p = "delete"
    print(act_p, num)
