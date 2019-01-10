class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def find(self, key):
        node = self._find(key)
        if node is not None:
            return (node.key, node.val)

    def _find(self, key):
        current = self.head
        while (current is not None):
            if current.key == key:
                return current
            current = current.next

    def _find_prev(self, key):
        if self.head.key == key:
            return None

        current = self.head
        while (current.next is not None):
            if current.next.key == key:
                return current
            current = current.next

    def add(self, key, val):
        node = Node(key, val)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while (current is not None):
                if current.key == key:
                    current.val = val
                    break

                elif current.next is None:
                    current.next = node
                    break

                current = current.next

    def remove(self, key):
        prev = self._find_prev(key)
        if prev is None:
            self.head = None
        else:
            if prev.next.next is None:
                prev.next = None
            else:
                prev.next = prev.next.next


class HashTable():
    def __init__(self, size=8):
        self.items = 0
        self.size = size
        self.table = []
        for _ in range(self.size):
            self.table.append(List())

    def _should_grow(self):
        return self.items >= self.size

    def _should_shrink(self):
        return self.items <= self.size / 2

    def _hash(self, key):
        return key % self.size

    def _resize(self, new_size):
        self.size = new_size
        new_table = []
        for _ in range(self.size):
            new_table.append(List())

        for bucket in self.table:
            current = bucket.head
            while (current is not None):
                new_bucket = self._hash(current.key)
                new_table[new_bucket].add(current.key, current.val)
                current = current.next

        self.table = new_table

    def _grow(self):
        self._resize(self.size * 2)

    def _shrink(self):
        self._resize(self.size / 2)

    def put(self, key, value):
        bucket = self._hash(key)
        self.table[bucket].add(key, value)
        self.items += 1

        if self._should_grow():
            self._grow()

    def get(self, key):
        bucket = self._hash(key)
        return self.table[bucket].find(key)

    def delete(self, key):
        bucket = self._hash(key)
        self.table[bucket].remove(key)
        self.items -= 1

        if self._should_shrink():
            self._shrink()


if __name__ == '__main__':
    table = HashTable()

    for i in range(100):
        table.put(i, 'foo' + str(i))

    for i in range(100):
        table.put(i, 'bar' + str(i))

    for i in range(10, 100):
        table.delete(i)

    for i in range(10):
        print table.get(i)
