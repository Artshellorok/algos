import random

n = 10**5
chosen = [0]*n
count = 0
print(n)
for i in range(n):
    key = random.randint(-10**9, 10**9)
    count += 1
    if count > 50000:
        l = -1
        r = -1
        print(key, l, r)
        continue

    while True:
        l = random.randint(0, n-1)
        if not chosen[l]:
            if l != 0:
                chosen[l] = True
            break
    while True:
        r = random.randint(0, n-1)
        if not chosen[r]:
            if r != 0:
                chosen[r] = True
            break
    print(key, l, r)
