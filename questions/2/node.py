class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        new_node = Node(data)
        n = self
        while n.next is not None:
            n = n.next
        n.next = new_node

    def traverse(self):
        thislevel = [self]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                print n.value,
        if n.left:
            nextlevel.append(n.left)
        if n.right:
            nextlevel.append(n.right)
        print
        thislevel = nextlevel

    def print_list(self):
        n = self
        ll = ""
        while n.next is not None:
            ll += str(n.data) + " -> "
            n = n.next
        print ll + str(n.data)
