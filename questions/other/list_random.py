from random import randint


class Node():
    def __init__(self, data):
        self.data = data
        self.idx = None
        self.next = None
        self.rand = None

    def append(self, data):
        new_node = Node(data)
        n = self
        while n.next is not None:
            n = n.next
        n.next = new_node

    def print_list_rand(self):
        n = self
        ll = ""
        i = 0
        while i < 20:
            ll += str(n.data) + " -> "
            n = n.rand
            i += 1
        print ll + str(n.data)

    def print_list(self):
        n = self
        ll = ""
        while n.next is not None:
            ll += str(n.data) + " -> "
            n = n.next
        print ll + str(n.data)


def copy_list(head):
    if head is None:
        return None

    copy_head = Node(head.data)
    copy_current = copy_head
    copy_array = []

    current = head.next
    i = 0
    while current is not None:
        copy_current.next = Node(current.data)
        copy_array.append(copy_current)
        copy_current = copy_current.next

        current.idx = i
        current = current.next
        i += 1

    i = 0
    current = head.next
    while current is not None:
        if current.rand.idx:
            copy_array[i].rand = copy_array[current.rand.idx]
        current = current.next
        i += 1

    return copy_head


if __name__ == "__main__":
    head = Node(3)
    for _ in range(10):
        head.append(randint(0, 10))

    # add nodes to array to randomly index them
    in_array = []
    current = head
    while current is not None:
        in_array.append(current)
        current = current.next

    current = head
    while current is not None:
        current.rand = in_array[randint(0, 10)]
        current = current.next

    copy = copy_list(head)

    head.print_list()
    copy.print_list()

    head.print_list_rand()
    copy.print_list_rand()
