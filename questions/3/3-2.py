class MinStack():

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x):
        self.stack.append(x)
        if len(self.min) == 0:
            self.min.append(x)
        elif x <= self.min[-1]:
            self.min.append(x)

    def pop(self):
        el = self.stack.pop()
        if len(self.min) and el == self.min[-1]:
            self.min.pop()

    def top(self):
        if len(self.stack):
            return self.stack[-1]
        return None

    def getMin(self):
        if len(self.min):
            return self.min[-1]
        return None
