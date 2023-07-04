import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

file = open('input.txt')
lines = file.readlines()
out = open("output.txt", "w")

# length of the bucket array
CAPACITY = 10000000

# node is a node of linked list (I just don't wanna create LinkedList class)


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return f"key: {self.key}, value: {self.value}, next: {self.next}"


class HashTable:
    def __init__(self):
        self.size = 0
        self.buckets = [None]*CAPACITY

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
        else:
            prev = node
            while node is not None:
                prev = Node
                node = node.next
            prev.next = Node(key, value)

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
                self.buckets[index] = node.next
            else:
                prev.next = node.next


table = HashTable()


def existsSubstringOfLengthK(s, t, k):
    # insert all k substrings to our hashtable
    for i in range(len(s) - k + 1):
        table.insert(s[i:k+i], i)
    for i in range(len(t) - k + 1):
        string = t[i:k+i]
        string_s = table.get(string)
        if string_s != None:
            return (string_s, i)
    return None


for i in range(len(lines)):
    s, t = lines[i].split()
    k = min(len(s), len(t))

    l = 0
    r = k
    m = 0
    mem = None
    while l <= r:
        m = (l + r) // 2

        res = existsSubstringOfLengthK(s, t, m)
        if res != None:
            mem = res
            l = m + 1

        else:
            r = m - 1
    out.write(str(mem[0]) + " " + str(mem[1]) + " " + str(r) + "\n")


print("Время выполнения: " + str(time.perf_counter() - t_start) + " секунд")
print("Использование памяти: " +
      str(tracemalloc.get_traced_memory()[1]) + " байт")
tracemalloc.stop()
