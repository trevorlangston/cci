class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class List:
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head

    # O(n)
    def find(self, val):
        current = self.head
        while (current is not None):
            if current.next.val == val:
                return current.next
            current = current.next

    # O(n)
    def nth(self, n):
        current = self.head
        for _ in range(n):
            if current is None:
                return None
            current = current.next

        return current

    # O(1)
    def add(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next

    # O(1)
    def remove(self, node):
        node.val = node.next.val
        node.next = node.next.next

    def reverse(self):
        self._reverse(self.head)
        # switch head and tail pointers
        temp = self.head
        self.head = self.tail
        self.tail = temp
        self.tail.next = None

    # O(n)
    def _reverse(self, node):
        if node.next is None:
            return
        self._reverse(node.next)
        node.next.next = node

    def print_list(self):
        current = self.head
        while (current is not None):
            print current.val
            current = current.next


if __name__ == "__main__":
    ll = List()
    for i in range(1, 10):
        ll.add(i)

    ll.remove(ll.find(5))
    ll.reverse()
    ll.print_list()

    for i in range(1, 10):
        ll.remove(i)
