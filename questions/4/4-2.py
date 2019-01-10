import node as n


def minimal_tree(arr):
    if not arr:
        return None

    mid = len(arr) / 2
    root = n.Node(arr[mid])
    root.left = minimal_tree(arr[:mid])
    root.right = minimal_tree(arr[mid+1:])

    return root


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    root = minimal_tree(arr)
    root.print_tree()
