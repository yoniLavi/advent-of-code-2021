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


def count_paths(edges, path, extra_visits=2):
    if not valid_path(path, extra_visits):
        return 0
    
    if path[-1] == 'end':
        return 1
    
    return sum(count_paths(edges, path + (dest,), extra_visits)
                           for source, dest in edges if source == path[-1])


if __name__ == '__main__':
    edges = process_edges([tuple(line.strip().split('-'))
                           for line in open("day12/input.txt")])
                           
    print(f'Part A: {count_paths(edges, ("start",), extra_visits=0)}')
    print(f'Part B: {count_paths(edges, ("start",), extra_visits=1)}')
