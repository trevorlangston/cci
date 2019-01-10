import node as n


def remove_dups(head):
    seen = {}
    curr = head
    prev = None

    while curr is not None:
        if curr.data in seen:
            prev.next = curr.next
        else:
            seen[curr.data] = None
            prev = curr
        curr = prev.next

    return head


if __name__ == "__main__":
    head = n.Node("Head")
    for i in range(10):
        head.append(i)
        head.append(i)

    head.print_list()
    head = remove_dups(head)
    head.print_list()
