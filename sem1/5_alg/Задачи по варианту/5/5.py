import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")


class Heap:
    memory = []
    key = 0
    val = 1

    def __init__(self, key=0, val=1):
        self.key = key
        self.val = val

    @property
    def size(self):
        return len(self.memory) - 1

    def push(self, num):
        key = self.key
        val = self.val
        self.memory.append(num)
        parent = (self.size - 1) // 2
        index = self.size
        while index > 0:
            if self.memory[parent][key] > self.memory[index][key]:
                self.memory[parent], self.memory[index] = self.memory[
                    index], self.memory[parent]
                index = parent
                parent = (index - 1) // 2
            elif self.memory[parent][key] == self.memory[index][key]:
                if self.memory[parent][val] > self.memory[index][val]:
                    self.memory[parent], self.memory[index] = self.memory[
                        index], self.memory[parent]
                    index = parent
                    parent = (index - 1) // 2
                else:
                    break
            else:
                break

    @property
    def min(self):
        if self.memory:
            return self.memory[0]
        else:
            return None

    def heapify(self):
        key = self.key
        val = self.val
        index = 0
        while 2 * index + 2 <= self.size:
            root = self.memory[index][key]
            root_val = self.memory[index][val]
            if self.memory[2 * index + 1][key] < self.memory[2 * index + 2][key]:
                minimum = 2 * index + 1
            elif self.memory[2 * index + 1][key] == self.memory[2 * index + 2][key]:
                if self.memory[2 * index + 1][val] < self.memory[2 * index + 2][val]:
                    minimum = 2 * index + 1
                else:
                    minimum = 2 * index + 2
            else:
                minimum = 2 * index + 2
            if self.memory[minimum][key] < root:
                self.memory[minimum], self.memory[index] = self.memory[
                    index], self.memory[minimum]
                index = minimum
            elif self.memory[minimum][key] == root:
                if self.memory[minimum][val] < root_val:
                    self.memory[minimum], self.memory[index] = self.memory[
                        index], self.memory[minimum]
                    index = minimum
                else:
                    break
            else:
                break
        if 2 * index + 1 <= self.size:
            root = self.memory[index][key]
            if self.memory[2 * index + 1][key] < root:
                self.memory[
                    2 * index +
                    1], self.memory[index] = self.memory[index], self.memory[
                        2 * index + 1]
            elif self.memory[2 * index + 1][key] == root:
                if self.memory[2 * index + 1][val] < root_val:
                    self.memory[
                        2 * index +
                        1], self.memory[index] = self.memory[index], self.memory[
                            2 * index + 1]

    def del_min(self):
        self.memory[0], self.memory[self.size] = self.memory[
            self.size], self.memory[0]
        self.memory.pop()
        self.heapify()


n, m = map(int, lines[0].split())
tasks = list(map(int, lines[1].split()))

threads = Heap(key="time", val="index")

for i in range(n):
    threads.push({
        "time": 0,
        "index": i
    })
count = 0
for task_time in tasks:
    thread = threads.min  # minimal available thread
    count += 1
    out.write(f"{thread['index']} {thread['time']}"+"\n")
    threads.del_min()

    # current thread will be available after completing the task
    threads.push({
        "time": thread["time"]+task_time,
        "index": thread["index"]
    })


print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
