import node as n
minimal_tree = __import__("4-2").minimal_tree


def validate_bst(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is not None:
            queue.append(node.left)
            queue.append(node.right)
            if node.left is not None and node.left.data > node.data:
                return False
            if node.right is not None and node.right.data <= node.data:
                return False
    return True


def validate_bst_recursive(root):
    left_valid = True
    if root.left is not None:
        if root.left.data > root.data:
            return False
        else:
            left_valid = validate_bst_recursive(root.left)

    right_valid = True
    if root.right is not None:
        if root.right.data <= root.data:
            return False
        else:
            right_valid = validate_bst_recursive(root.left)

    return left_valid and right_valid


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    root = minimal_tree(arr)
    print validate_bst(root)
    print validate_bst_recursive(root)

    root = n.Node(100)
    root.left = n.Node(200)
    print validate_bst(root)
    print validate_bst_recursive(root)
