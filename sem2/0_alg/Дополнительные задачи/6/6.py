import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")


def swap(i, j):
    d = a[i]
    a[i] = a[j]
    a[j] = d


def cmp(a, b):
    if len(a) > len(b):
        mini = len(b)
        first = int(a[:mini])
        second = int(b)
        if first > second:
            return True
        else:
            return False
    elif len(b) > len(a):
        mini = len(a)
        first = int(a)
        second = int(b[:mini])
        if second > first:
            return False
        else:
            return True
    else:
        if int(a) > int(b):
            return True
        else:
            return False


def quick_sort(l, r):
    i = l
    j = r
    pivot = nums[(i+j)//2]
    while i <= j:
        while cmp(nums[i], pivot):
            i += 1
        while cmp(pivot, nums[j]) and (pivot != nums[j]):
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    if j > l:
        quick_sort(l, j)
    if i < r:
        quick_sort(i, r)


n = int(lines[0])
nums = list(map(str, lines[1].split()))
quick_sort(0, n-1)
out.write("".join(nums))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
