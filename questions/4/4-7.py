def find_order(projects, dependencies):
    if len(projects) <= 1:
        return projects

    adj_list = build_adj_list(projects, dependencies)
    return build_order(adj_list)


def build_adj_list(projects, dependencies):
    adj_list = {}
    for p in projects:
        adj_list[p] = {'next': [], 'inbound': 0}

    for d in dependencies:
        adj_list[d[0]]['next'].append(d[1])
        adj_list[d[1]]['inbound'] += 1

    return adj_list


def build_order(adj_list):
    order = []
    for project in adj_list:
        if adj_list[project]['inbound'] == 0:
            order.append(project)

    if len(order) == 0:
        raise ValueError('No build order exists')

    cur = 0
    while cur < len(order):
        p = order[cur]
        for n in adj_list[p]['next']:
            if adj_list[n]['inbound'] < 1:
                raise ValueError('No build order exists')
            else:
                adj_list[n]['inbound'] -= 1
                if adj_list[n]['inbound'] == 0:
                    order.append(n)
        cur += 1

    if len(order) < len(adj_list.keys()):
        raise ValueError('No build order exists')
    else:
        return order


if __name__ == "__main__":
    projects = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    dependencies = [('C', 'F'), ('F', 'D'), ('B', 'D'), ('A', 'B'), ('E', 'C'), ('A', 'C'), ('B', 'C'), ('A', 'E')]
    print find_order(projects, dependencies)

    projects = ['A', 'B', 'C']
    dependencies = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    print find_order(projects, dependencies)

    projects = ['A', 'B', 'C', 'D']
    dependencies = [('D', 'A'), ('A', 'B'), ('B', 'C'), ('C', 'A')]
    print find_order(projects, dependencies)
