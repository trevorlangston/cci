from random import randint


class SortStack():
    def __init__(self):
        self.sorted = []
        self.buffer = []

    def push(self, x):
        if len(self.sorted) == 0:
            self.sorted.append(x)
        else:
            count = 0
            while len(self.sorted) > 0 and self.sorted[-1] > x:
                self.buffer.append(self.sorted.pop())
                count += 1
            self.sorted.append(x)
            for _ in range(count):
                self.sorted.append(self.buffer.pop())

    def pop(self):
        return self.sorted.pop()


if __name__ == "__main__":
    stack = SortStack()
    for _ in range(10):
        stack.push(randint(0, 10))
    for _ in range(10):
        print stack.pop()
