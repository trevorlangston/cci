class SetOfStacks():
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError('Capacity must be greater than 0')

        self.stacks = []
        self.capacity = capacity
        self.cur = 0

    def push(self, x):
        stack = self.cur // self.capacity
        if stack == len(self.stacks):
            self.stacks.append([x])
        else:
            self.stacks[stack].append(x)
        self.cur += 1

    def pop(self):
        stack = (self.cur - 1) // self.capacity
        self.cur -= 1
        return self.stacks[stack].pop()


if __name__ == "__main__":
    stack = SetOfStacks(2)
    for i in range(10):
        stack.push(i)
    for _ in range(10):
        print stack.pop()
