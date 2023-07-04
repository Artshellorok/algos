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
        self.memory.pop()

    @property
    def top(self):
        try:
            return self.memory[-1]
        except:
            return (None, None)

    @property
    def len(self):
        return len(self.memory)


s = Stack()

seq = lines[0]
n = len(seq)

allowed = "({[]})"
closing = "]})"
open_for_close = {
    "]": "[",
    "}": "{",
    ")": "(",
}

out = open("output.txt", 'w')

for i in range(n):
    el = seq[i]
    if el in allowed:
        if el not in closing:
            s.add((seq[i], i+1))
        else:
            if open_for_close[el] == s.top[0]:
                s.pop()
            else:
                out.write(str(i+1))
                print("Время выполнения: " +
                      str(time.perf_counter() - t_start) + " секунд")
                print("Использование памяти: " +
                      str(tracemalloc.get_traced_memory()[1]) + " байт")
                tracemalloc.stop()
                exit()
if s.len > 0:
    out.write(str(s.top[1]))
    print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
    print("Использование памяти: " +
          str(tracemalloc.get_traced_memory()[1]) + " байт")
    tracemalloc.stop()
    exit()
else:
    out.write("Success")

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
