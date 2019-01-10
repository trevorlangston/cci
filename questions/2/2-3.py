import node as n

if __name__ == "__main__":

    head = n.Node(-1)
    for i in range(10):
        head.append(i)

    curr = head
    for _ in range(5):
        curr = curr.next

    head.print_list()

    curr.data = curr.next.data
    curr.next = curr.next.next

    head.print_list()
