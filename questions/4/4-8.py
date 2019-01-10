import node as n


def first_common_ancestor(node_a, node_b):
    if node_a.data == node_b.data:
        return node_a

    if node_a.data > node_b.data:
        temp = node_a
        node_a = node_b
        node_b = temp

    if tree_has_node(node_a.right, node_b):
        return node_a

    elif tree_has_node(node_b.left, node_a):
        return node_b
    else:
        current = node_a
        while current.parent:
            current = current.parent
            if current.data > node_a.data:
                if tree_has_node(current.right, node_b):
                    return current

        return None


def tree_has_node(root, node):
    if root is None:
        return False

    while root is not None:
        if root.data == node.data:
            return True
        elif root.data > node.data:
            root = root.left
        else:
            root = root.right

    return False


if __name__ == "__main__":
    root = n.Node(4)

    root.left = n.Node(2)
    root.left.parent = root

    root.left.left = n.Node(1)
    root.left.left.parent = root.left

    root.left.left = n.Node(1)
    root.left.left.parent = root.left

    root.left.left.left = n.Node(0)
    root.left.left.left.parent = root.left.left

    root.left.right = n.Node(3)
    root.left.right.parent = root.left

    root.right = n.Node(7)
    root.right.parent = root

    root.right.right = n.Node(8)
    root.right.right.parent = root.right

    root.right.left = n.Node(6)
    root.right.left.parent = root.right

    root.right.left.left = n.Node(5)
    root.right.left.left.parent = root.right.left

    a = root.left.right
    b = root.right.left.left

    print first_common_ancestor(a, b).data
    print first_common_ancestor(b, a).data

    a = root.left.left.left
    b = root.left.right

    print first_common_ancestor(a, b).data
    print first_common_ancestor(b, a).data

    a = root.right
    b = root.right.right

    print first_common_ancestor(a, b).data
    print first_common_ancestor(b, a).data

    a = root.left
    b = root.left.left

    print first_common_ancestor(a, b).data
    print first_common_ancestor(b, a).data
