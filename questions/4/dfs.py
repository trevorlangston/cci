def dfs_iter(graph, start):
    visited = set()
    stack = [start]  # convert to bfs by using a queue
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for next in graph[node]:
                if next not in visited:
                    stack.append(next)
    return visited


def dfs_rec(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    for next in graph[node]:
        if next not in visited:
            dfs_rec(graph, next, visited)

    return visited


class Paths():
    def __init__(self):
        self.paths = []

    def add(self, path):
        self.paths.append(path)


def dfs_iter_paths(graph, start, goal):
    stack = [(start, [start])]
    paths = []
    while stack:
        (node, path) = stack.pop()
        for next in graph[node]:
            if next == goal:
                paths.append(path + [next])
            else:
                if next not in path:
                    stack.append((next, path + [next]))
    return paths


def dfs_rec_paths(graph, start, end, paths, current_path=[]):
    current_path = current_path + [start]
    if start == end:
        paths.add(current_path)
    for node in graph[start]:
        if node not in current_path:
            dfs_rec_paths(graph, node, end, paths, current_path)


def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        visited.add(node)
        for next in graph[node]:
            if next not in visited:
                queue.append(next)
    return visited


def bfs_paths(graph, start, goal):
    paths = []
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for next in graph[node]:
            if next == goal:
                paths.append(path + [next])
            elif next not in set(path):
                queue.append((next, path + [next]))
    return paths


if __name__ == "__main__":
    graph = {
            'A': set(['B', 'C']),
            'B': set(['A', 'D', 'E']),
            'C': set(['A', 'F']),
            'D': set(['B']),
            'E': set(['B', 'F']),
            'F': set(['C', 'E'])
            }

    print "DFS"
    print "visit every node"
    print list(dfs_iter(graph, 'A'))
    print list(dfs_rec(graph, 'A'))

    # get paths from start to end
    print "get paths from A to F"
    paths = Paths()
    print dfs_iter_paths(graph, 'A', 'F')

    paths = Paths()
    dfs_rec_paths(graph, 'A', 'F', paths)
    print paths.paths

    print "\nBFS"
    print "visit every node"
    print bfs(graph, 'A')

    print "get paths from A to F"
    print bfs_paths(graph, 'A', 'F')
