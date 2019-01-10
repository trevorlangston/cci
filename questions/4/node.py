class Node():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def add(self, data):
        if self is None:
            self.data = data

        if data <= self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add(data)

    def is_leaf(self):
        return not self.left and not self.right

    def print_tree(self):
        queue = [self]
        while queue:
            current = queue.pop(0)
            if current is not None:
                print current.data
                queue.append(current.left)
                queue.append(current.right)


if __name__ == "__main__":
    n = Node(5)
    for i in range(10):
        n.add(i)

    n.print_tree()
