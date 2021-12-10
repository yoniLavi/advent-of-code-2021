from collections import Counter
from itertools import count


basin_id_provider = count(10)


def neighbour_indices(r, c, rows, cols):
    indices = []
    if r > 0:
        indices.append([r-1, c])
    if r < rows-1:
        indices.append([r+1, c])
    if c > 0:
        indices.append([r, c-1])
    if c < cols-1:
        indices.append([r, c+1])
    return indices


def day9a(heightmap):
    risk_level = 0
    for r in range(len(heightmap)):
        for c in range(len(heightmap[0])):
            neighbour_positions = neighbour_indices(r, c, len(heightmap), len(heightmap[0]))
            min_neighbour = min(heightmap[r][c] for r, c in neighbour_positions)
            if heightmap[r][c] < min_neighbour:
                risk_level += 1 + heightmap[r][c]
    return risk_level


def tag_basin(heightmap, r0, c0, basin_id):
    heightmap[r0][c0] = basin_id
    for r, c in neighbour_indices(r0, c0, len(heightmap), len(heightmap[0])):
        if heightmap[r][c] < 9:
            tag_basin(heightmap, r, c, basin_id)


def day9b(heightmap):
    for r in range(len(heightmap)):
        for c in range(len(heightmap[0])):
            if heightmap[r][c] < 9:
                tag_basin(heightmap, r, c, next(basin_id_provider))
    
    top_basins = Counter(filter(lambda x: x != 9, sum(heightmap, [])))
    output_product = 1
    for _, basin_size in top_basins.most_common(3):
        output_product *= basin_size
    return output_product


if __name__ == "__main__":
    heightmap = [list(map(int, line.strip())) for line in open('day9/input.txt')]
    print(f'Part A: {day9a(heightmap)}')
    print(f'Part B: {day9b(heightmap)}')
