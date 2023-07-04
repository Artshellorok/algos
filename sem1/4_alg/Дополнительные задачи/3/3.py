import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()

out = open("output.txt", 'w')


class Stack:
    memory = []

    def __init__(self):
        self.memory = []

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


n = int(lines[0])

allowed = "([])"
closing = "])"
open_for_close = {
    "]": "[",
    ")": "("
}
for _i in range(n):
    seq = lines[_i+1]
    m = len(seq)
    s = Stack()
    fail = False
    for i in range(m):
        el = seq[i]
        if el in allowed:
            if el not in closing:
                s.add((seq[i], i+1))
            else:
                if open_for_close[el] == s.top[0]:
                    s.pop()
                else:
                    out.write("NO\n")
                    fail = True
                    break
    if not fail:
        if s.len > 0:
            out.write("NO\n")
        else:
            out.write("YES\n")

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
