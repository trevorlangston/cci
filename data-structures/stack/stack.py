# single linked list
class Item:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack2:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def peak(self):
        return self.top

    def push(self, val):
        new_item = Item(val)
        if self.top is None:
            self.top = new_item
        else:
            new_item.next = self.top
            self.top = new_item

    def pop(self):
        if self.top is None:
            return None

        popped = self.top
        self.top = self.top.next
        return popped.val


# abstraction on python list
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def peak(self):
        return self.stack[-1]

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack):
            return self.stack.pop()
        return None


if __name__ == "__main__":
    print "python list implementation"
    st = Stack()
    for i in range(10):
        st.push(i)

    for i in range(10):
        print st.pop()

    print "\nlinked list implementation"
    st2 = Stack()
    for i in range(10, 20):
        st2.push(i)

    for i in range(10, 20):
        print st2.pop()
