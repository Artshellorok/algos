import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()


class Queue:
    memory = []
    head = 0
    tail = 0
    length = -1
    count = 0

    def __init__(self, n):
        self.length = (n+1)
        self.memory = [None] * (n+1)

    def enqueue(self, el):
        self.memory[self.tail] = el
        if self.tail == self.length - 1:
            self.tail = 0
        else:
            self.tail += 1
        if self.tail == self.head:
            raise Exception("Nicht genug Speicher! Scheiße!")
        self.count += 1

    def dequeue(self):
        self.memory[self.head] = None

        if self.head == self.length - 1:
            self.head = 0
        else:
            self.head += 1
        self.count -= 1

    @property
    def top(self):
        return self.memory[self.head]

    @property
    def len(self):
        return self.count


n = int(lines[0])
s = Queue(n)
h, m, tolerance = map(int, lines[1].split())

out = open("output.txt", "w")

unixtime = h * 60 + m + 10
s.enqueue((unixtime//60, unixtime % 60))
out.write(f"{unixtime//60} {unixtime % 60}\n")

for i in range(1, n):
    h, m, tolerance = map(int, lines[i+1].split())
    h1, m1 = s.top

    unixtime1 = h*60+m
    unixtime2 = h1*60+m1

    while unixtime1 > unixtime2:
        s.dequeue()
        if s.len == 0:
            unixtime2 = unixtime1
            break
        h1, m1 = s.top
        unixtime1 = h*60+m

    if tolerance >= s.len:
        unixtime2 += 10
        h = unixtime2 // 60
        m = unixtime2 % 60
        s.enqueue((h, m))
        out.write(f"{h} {m}\n")
    else:
        out.write(f"{h} {m}\n")

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
