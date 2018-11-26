# doubly linked list - makes dequeueing easier
class Item:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.front = None
        self.end = None

    def enqueue(self, val):
        new_item = Item(val)
        if self.end is None:
            self.end = new_item
            self.front = new_item
        else:
            new_item.next = self.end
            self.end.prev = new_item
            self.end = new_item

    def dequeue(self):
        if self.front is None:
            return None

        item = self.front
        self.front = self.front.prev
        if self.front is not None:
            self.front.next = None
        return item.val


if __name__ == "__main__":
    q = Queue()
    for i in range(10):
        q.enqueue(i)

    for i in range(10):
        print q.dequeue()
