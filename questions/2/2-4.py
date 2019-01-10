import node as n


def partition_new(head, num):
    less = n.Node(0)
    more = n.Node(0)

    current = head
    while current is not None:
        if current.data < num:
            less.append(current.data)
        else:
            more.append(current.data)
        current = current.next

    less = less.next
    more = more.next
    current = less
    while current.next is not None:
        current = current.next
    current.next = more

    return less


def partition_new2(head, num):
    new_middle = n.Node(0)
    new_head = new_tail = new_middle

    current = head
    while current is not None:
        node = n.Node(current.data)
        if current.data < num:
            node.next = new_head
            new_head = node
        else:
            new_tail.next = node
            new_tail = node
        current = current.next

    new_middle.data = new_middle.next.data
    new_middle.next = new_middle.next.next

    return new_head


def partition_in_place(head, num):
    list_length = 0
    current = head
    while current is not None:
        current = current.next
        list_length += 1

    idx = 0
    swaps = 0
    current = head

    while idx < list_length - swaps:
        if current.data < num:
            current = current.next
            idx += 1
        else:
            runner = current
            for _ in range(list_length - swaps - idx - 1):
                temp = runner.data
                runner.data = runner.next.data
                runner.next.data = temp
                runner = runner.next
            swaps += 1


if __name__ == "__main__":
    head = n.Node(3)
    head.append(5)
    head.append(8)
    head.append(5)
    head.append(4)
    head.append(-1)
    head.append(10)
    head.append(2)
    head.append(1)

    head.print_list()

    partition_in_place(head, 6)
    new = partition_new(head, 6)
    new2 = partition_new2(head, 6)

    head.print_list()
    new.print_list()
    new2.print_list()
