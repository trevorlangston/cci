class Queue():
    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def push(self, x):
        self.stack_a.append(x)

    def pop(self):
        if len(self.stack_b) == 0:
            while len(self.stack_a) > 0:
                self.stack_b.append(self.stack_a.pop())
        return self.stack_b.pop()


if __name__ == "__main__":
    q = Queue()
    for i in range(10):
        q.push(i)
    for _ in range(10):
        print q.pop()
