import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")


def operate(num1, op, num2):
    if op == "-":
        return num1 - num2
    elif op == "+":
        return num1 + num2
    else:
        return num1 * num2


def dp_max(start, end):
    maxi = -999999999
    if start == end:
        return nums[start]
    for k in range(start, end):
        val = max(operate(dp_max(start, k), ops[k], dp_max(k+1, end)),
                  operate(dp_max(start, k), ops[k], dp_min(k+1, end)),
                  operate(dp_min(start, k), ops[k], dp_max(k+1, end)),
                  operate(dp_min(start, k), ops[k], dp_min(k+1, end)))
        if val > maxi:
            maxi = val
    return maxi


def dp_min(start, end):
    mini = 99999999999
    if start == end:
        return nums[start]
    for k in range(start, end):
        val = min(operate(dp_max(start, k), ops[k], dp_max(k+1, end)),
                  operate(dp_max(start, k), ops[k], dp_min(k+1, end)),
                  operate(dp_min(start, k), ops[k], dp_max(k+1, end)),
                  operate(dp_min(start, k), ops[k], dp_min(k+1, end)))
        if val < mini:
            mini = val
    return mini


string = lines[0]
nums = []
ops = []
for i in range(len(string)):
    if i % 2 == 0:
        nums.append(int(string[i]))
    else:
        ops.append(string[i])
out.write(str(dp_max(0, len(nums)-1)))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
