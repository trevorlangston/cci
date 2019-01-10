import node as n


def sequences(root):
    if root is None:
        return []

    if root.is_leaf():
        return [root.data]

    left = sequences(root.left)
    right = sequences(root.right)
    print root.data
    print left
    print right
    print "\n"

    return [[root.data] + left + right, [root.data] + right + left]


if __name__ == "__main__":
    root = n.Node(2)
    root.left = n.Node(1)
    root.right = n.Node(4)
    root.right.right = n.Node(3)
    root.right.left = n.Node(5)
    print sequences(root)
