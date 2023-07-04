import math
import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt', 'r')
lines = file.readlines()
f = open('output.txt', 'w')


def merge(x, y, key):
    result = []
    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i][key] > y[j][key]:
            result.append(y[j])
            j += 1
        else:
            result.append(x[i])
            i += 1
    result += x[i:]
    result += y[j:]
    return result


def mergeSort(arr, key):
    if len(arr) >= 2:
        pivot = len(arr)//2
        arr1 = mergeSort(arr[:pivot], key)
        arr2 = mergeSort(arr[pivot:], key)
        return merge(arr1, arr2, key)
    else:
        return arr


def distance(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


def distThree(points):
    min_dist = 99999999
    p1 = None
    p2 = None
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                dist = distance(points[i], points[j])
                if dist < min_dist:
                    min_dist = dist
                    p1 = points[i]
                    p2 = points[j]
    return [p1, p2, min_dist]


def recursion(x_sort, y_sort):
    n = len(x_sort)
    if n <= 3:
        return distThree(x_sort)
    else:
        pivot = x_sort[n//2]
        xl = x_sort[:n//2]
        xr = x_sort[n//2:]
        yl = []
        yr = []
        for point in y_sort:
            if (point[0] <= pivot[0]):
                yl.append(point)
            else:
                yr.append(point)
        p1_left, p2_left, dist_left = recursion(xl, yl)
        p1_right, p2_right, dist_right = recursion(xr, yr)
        if dist_left < dist_right:
            p1 = p1_left
            p2 = p2_left
            dist = dist_left
        else:
            p1 = p1_right
            p2 = p2_right
            dist = dist_right
        mid = []
        for point in y_sorted:
            if (pivot[0] - dist < point[0]) and (pivot[0] + dist > point[0]):
                mid.append(point)
        # go through all the middle elements
        for i in range(len(mid)):
            # consider only 4 neighbour elements, since only 4 can be placed in the distance of d (or all which are left)
            for j in range(i + 1, min(i + 5, len(mid))):
                d = distance(mid[i], mid[j])
                if d < dist:
                    p1 = mid[i]
                    p2 = mid[j]
                    dist = d
        return [p1, p2, dist]


n = int(lines[0])
if n == 1:
    f.write(str(-1))
    f.close()
    print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
    print("Использование памяти: " +
          str(tracemalloc.get_traced_memory()[1]) + " байт")
    tracemalloc.stop()
    exit()
points = []
for i in range(n):
    points.append(list(map(int, lines[i+1].split())))

x_sorted = mergeSort(points, 0)
y_sorted = mergeSort(points, 1)

f.write(str(recursion(x_sorted, y_sorted)[2]))
f.close()

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
