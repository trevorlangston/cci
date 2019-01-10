class Vector():
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.vec = [None] * self.capacity

    def grow_as_needed(self):
        if self.size == self.capacity:
            self.vec += [None] * self.capacity
            self.capacity *= 2

    def shrink_as_needed(self):
        if self.size == self.capacity / 4 - 1:
            self.capacity /= 2
            self.vec = self.vec[:self.capacity]

    def append(self, item):
        self.vec[self.size] = item
        self.size += 1
        self.grow_as_needed()

    def pop(self):
        self.vec[self.size] = None
        self.size -= 1
        self.shrink_as_needed()


if __name__ == "__main__":
    v = Vector()
    for i in range(16):
        v.append(i)
        print v.vec

    for _ in range(16):
        v.pop()
        print v.vec
