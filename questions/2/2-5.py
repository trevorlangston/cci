import node as n


def sum(head_a, head_b):
    curr_a = head_a
    curr_b = head_b

    total = ""
    carry = 0

    while True:
        t = carry

        if curr_a is not None:
            t += curr_a.data
            curr_a = curr_a.next

        if curr_b is not None:
            t += curr_b.data
            curr_b = curr_b.next

        if t == 0:
            break

        if t > 10:
            carry = 1
            t -= 10
        else:
            carry = 0

        total = str(t) + total

    return int(total)


if __name__ == "__main__":

    head_a = n.Node(5)
    head_a.append(4)
    head_a.append(9)
    head_a.append(0)
    head_a.append(0)

    head_b = n.Node(7)
    head_b.append(2)
    head_b.append(6)
    head_b.append(3)

    head_a.print_list()
    head_b.print_list()

    print sum(head_a, head_b)
