import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()


class Stack:
    memory = []

    def add(self, el):
        self.memory.append(el)

    def pop(self):
        del self.memory[-1]

    @property
    def top(self):
        try:
            return self.memory[-1]
        except:
            raise Exception("No elements in stack memory")


s = Stack()

n = int(lines[0])

out = []

for i in range(n):
    inputs = lines[i+1]
    if inputs[0] == "+":
        el = inputs.split()[1]
        s.add(el)
    else:
        out.append(s.top)
        s.pop()
open("output.txt", 'w').write("\n".join(map(str, out)))

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
