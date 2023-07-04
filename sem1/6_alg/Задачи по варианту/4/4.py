import time
import tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

# length of the bucket array
CAPACITY = 1000000

# node is a node of linked list (I just don't wanna create LinkedList class)


class Node:
    def __init__(self, key, value, prev=None, next_out=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next_out = next_out
        self.next = None

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return f"'key': {self.key}, 'value': {self.value}"


class HashTable:
    def __init__(self):
        self.size = 0
        self.buckets = [None]*CAPACITY
        self.top = None

    def hash(self, key):
        summ = 0
        for i in range(len(key)):
            summ += (ord(key[i])) * (125 ** i)

        return summ % CAPACITY

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            if self.top is not None:
                self.buckets[index].prev = self.top
                self.top.next_out = self.buckets[index]
            self.top = self.buckets[index]
        else:
            prev = node
            while node is not None:
                if prev.key == key:
                    prev.value = value
                    return
                prev = Node
                node = node.next
            prev.next = Node(key, value)
            if self.top is not None:
                prev.next.prev = self.top.value
            self.top.next_out = prev.next
            self.top = prev.next

    def next(self, key):
        index = self.hash(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        return node.next_out if node is not None else None

    def prev(self, key):
        index = self.hash(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        return node.prev if node is not None else None

    def get(self, key):
        index = self.hash(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        return node.value if node is not None else None

    def exists(self, key):
        return True if self.get(key) != None else False

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]

        # persist previous element, so we can remove linked list node
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is not None:
            self.size -= 1
            if prev is None:
                if self.top == node:
                    self.top = node.prev
                if node.next_out is not None:
                    if node.prev is not None:
                        node.prev.next_out = node.next_out
                    try:
                        node.next_out.prev = node.prev
                    except Exception:
                        print(node.prev)
                        print(node.next_out)
                else:
                    if node.prev is not None:
                        node.prev.next_out = None
                self.buckets[index] = node.next
            else:
                if self.top == node:
                    self.top = node.prev
                if node.next_out is not None:
                    if node.prev is not None:
                        node.prev.next_out = node.next_out
                    node.next_out.prev = node.prev
                else:
                    if node.prev is not None:
                        node.prev.next_out = None
                prev.next = node.next


table = HashTable()
n = int(lines[0])
for i in range(n):
    inputs = lines[i+1].split()
    key = inputs[1]
    match inputs[0]:
        case "put":
            val = inputs[2]
            table.insert(key, val)
        case "delete":
            table.remove(key)
        case "next":
            output = table.next(key)
            if output is None:
                out.write("<none>\n")
            else:
                out.write(str(output.value) + "\n")
        case "prev":
            output = table.prev(key)
            if output is None:
                out.write("<none>\n")
            else:
                out.write(str(output.value) + "\n")
        case "get":
            val = table.get(key)
            if val == None:
                out.write("<none>\n")
            else:
                out.write(str(val) + "\n")

print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
