import node as n


def is_palindrome(head):
    reversed = None

    current = head
    while current is not None:
        node = n.Node(current.data)
        node.next = reversed
        reversed = node
        current = current.next

    current = head
    while current is not None:
        if current.data != reversed.data:
            return False
        current = current.next
        reversed = reversed.next

    return True


if __name__ == "__main__":
    head = n.Node(3)
    head.append(5)
    head.append(8)
    head.append(5)
    head.append(3)

    print is_palindrome(head) is True
