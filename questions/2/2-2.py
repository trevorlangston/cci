import node as n


class Helper():
    def __init__(self):
        self.count = 0
        self.ans = None


def kth_last_rec(head, k, helper):
    if head.next is not None:
        kth_last_rec(head.next, k, helper)

    helper.count += 1
    if helper.count == k:
        helper.ans = head


def kth_last_iter(head, k):
    curr = head
    sec = head

    while k > 0:
        k -= 1
        curr = curr.next

    while curr is not None:
        curr = curr.next
        sec = sec.next

    return sec


if __name__ == "__main__":
    k = 2
    head = n.Node(-1)
    for i in range(10):
        head.append(i)

    head.print_list()

    helper = Helper()
    kth_last_rec(head, k, helper)
    print helper.ans.data

    print kth_last_iter(head, k).data

