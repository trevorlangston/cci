minimal_tree = __import__("4-2").minimal_tree


class ListNode():
    def __init__(self, data):
        self.data = data
        self.next = None

    def add(self, node):
        current = self
        while current is not None:
            current = current.next
        current = node

    def print_list(self):
        current = self
        while current is not None:
            print str(current.data) + " -> "
            current = current.next


def list_of_depths(root):
    level = 0
    levels = []
    queue = [(root, level)]
    while queue:
        (node, level) = queue.pop(0)
        if node is not None:
            if level < len(levels):
                levels[level].append(node.data)
            else:
                levels.append([node.data])
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
    return levels


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    root = minimal_tree(arr)
    levels = list_of_depths(root)
    print levels
