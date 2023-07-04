import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")


def obMoeglich(n, a, b, c):
    if a == 0 and b == 0 and c == 0:
        return True
    if n < 0:
        return False

    if a >= nums[n]:
        if obMoeglich(n-1, a - nums[n], b, c):
            return True

    if b >= nums[n]:
        if obMoeglich(n-1, a, b - nums[n], c):
            return True

    if c >= nums[n]:
        if obMoeglich(n-1, a, b, c - nums[n]):
            return True

    return False


n = int(lines[0])
nums = list(map(int, lines[1].split()))
s = sum(nums) // 3
if sum(nums) % 3 != 0:
    out.write("0")
else:
    out.write(str(int(obMoeglich(n-1, s, s, s))))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
