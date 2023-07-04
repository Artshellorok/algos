import copy
import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

n = int(lines[0]) - 1
arr = {
    "0": 0,
    "1": 1,
    "2": 1,
    "3": 1,
    "4": 1,
    "5": 1,
    "6": 1,
    "7": 1,
    "8": 0,
    "9": 1
}
arr_new = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0
}
for i in range(n):
    arr_new["0"] = arr["4"] + arr["6"]
    arr_new["1"] = arr["8"] + arr["6"]
    arr_new["2"] = arr["7"] + arr["9"]
    arr_new["3"] = arr["8"] + arr["4"]
    arr_new["4"] = arr["0"] + arr["9"] + arr["3"]
    arr_new["6"] = arr["0"] + arr["7"] + arr["1"]
    arr_new["7"] = arr["6"] + arr["2"]
    arr_new["8"] = arr["3"] + arr["1"]
    arr_new["9"] = arr["4"] + arr["2"]
    arr = copy.deepcopy(arr_new)
    arr_new = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0
    }
summ = 0
for key in arr_new:
    summ += arr[key]
out.write(str(summ))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
