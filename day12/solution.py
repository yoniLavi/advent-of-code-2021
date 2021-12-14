def process_edges(edges):
    for i in range(len(edges)):
        if edges[i][1] == 'start':
            edges[i] = edges[i][::-1]
        elif edges[i][0] != 'start' and edges[i][1] != 'end':
            edges.append(edges[i][::-1])
    return edges


def valid_path(path, extra_visits=0):
    return sum(max(0, path.count(node) - 1) for node in set(path)
               if node.islower()) <= extra_visits


def dfs_count_paths(edges, extra_visits=2):
    path_count = 0
    dfs_stack = [t for t in edges if t[0] == 'start']
    while dfs_stack:
        partial_path = dfs_stack.pop()
        for next_node in (t[1] for t in edges if t[0] == partial_path[-1]):
            path = partial_path + (next_node,)
            if next_node == 'end':
                path_count += 1
            elif valid_path(path, extra_visits):
                dfs_stack.append(path)
    return path_count


if __name__ == '__main__':
    edges = process_edges([tuple(line.strip().split('-'))
                           for line in open("day12/input.txt")])
    print(f'Part A: {dfs_count_paths(edges, extra_visits=0)=}')
    print(f'Part B: {dfs_count_paths(edges, extra_visits=1)=}')
