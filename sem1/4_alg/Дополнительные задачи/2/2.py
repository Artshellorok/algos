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

    def __init__(self, n):
        self.length = n+1
        self.memory = [None] * (n+1)

    def enqueue(self, el):
        self.memory[self.tail] = el
        if self.tail == self.length - 1:
            self.tail = 0
        else:
            self.tail += 1
        if self.tail == self.head:
            raise Exception("Nicht genug Speicher! Scheiße!")

    def dequeue(self):
        if self.head == self.tail:
            raise Exception("Scheßie! Es gibt keine Elementen im Queue mehr!")
        el = self.memory[self.head]
        self.memory[self.head] = None

        if self.head == self.length - 1:
            self.head = 0
        else:
            self.head += 1
        return el


n = int(lines[0])
s = Queue(n)
out = open("output.txt", "w")

for i in range(n):
    inputs = lines[i+1]
    if inputs[0] == "+":
        el = inputs.split()[1]
        s.enqueue(el)
    else:
        out.write(f"{s.dequeue()}\n")

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
