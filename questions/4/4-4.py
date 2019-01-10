import node as n
import sys

minimal_tree = __import__("4-2").minimal_tree


def check_balanced(root):
    stack = [(0, root)]
    level_seen = None
    while stack:
        (level, node) = stack.pop()
        if node is None:
            if level_seen is None:
                level_seen = level
            else:
                if abs(level_seen - level) > 1:
                    return False
        else:
            stack.append((level + 1, node.left))
            stack.append((level + 1, node.right))

    return True


class Helper():
    def __init__(self):
        self.heights = []

    def add(self, height):
        self.heights.append(height)

    def is_balanced(self):
        seen = None
        for height in self.heights:
            if seen is None:
                seen = height
            else:
                if abs(height - seen) > 1:
                    return False

        return True


def check_balanced_recursive(root):
    h = Helper()
    helper(root, 0, h)
    return h.is_balanced()


def helper(root, level, h):
    if root is None:
        h.add(level)
    else:
        helper(root.left, level + 1, h)
        helper(root.right, level + 1, h)


def check_balanced_recursive2(root):
    min_int = -sys.maxint - 1
    return check_height(root) != min_int


# TODO not working
def check_height(root):
    if root is None:
        return -1

    min_int = -sys.maxint - 1

    left_height = check_height(root.left)
    if left_height == min_int:
        return min_int

    right_height = check_height(root.left)
    if right_height == min_int:
        return min_int

    if abs(left_height - right_height) > 1:
        return min_int
    else:
        return max(left_height, right_height) + 1


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    root = minimal_tree(arr)
    print check_balanced(root)
    print check_balanced_recursive(root)
    print check_balanced_recursive2(root)

    root = n.Node(100)
    for num in arr:
        root.add(num)

    print check_balanced(root)
    print check_balanced_recursive(root)
    print check_balanced_recursive2(root)
