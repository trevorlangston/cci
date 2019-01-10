class Item:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.end = None

    def peak(self):
        return self.front

    def is_empty(self):
        return self.front is None

    def add(self, val):
        new_item = Item(val)
        if self.end is None:
            self.end = new_item
            self.front = new_item
        else:
            self.end.next = new_item
            self.end = self.end.next

    def remove(self):
        if self.front is None:
            return None

        item = self.front
        if self.front.next is not None:
            self.front = self.front.next

        return item.val


if __name__ == "__main__":
    q = Queue()
    for i in range(10):
        q.add(i)

    for i in range(10):
        print q.remove()
