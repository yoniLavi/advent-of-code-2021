import numpy as np


def indices_between(a, b):
    if a == b:
        return a
    elif a < b:
        return list(range(a, b + 1))
    else:
        return list(range(a, b - 1, -1))


def count_overlaps(lines, size=1000):
    ocean_floor = np.zeros((size, size))
    for x1, x2, y1, y2 in lines:
        ocean_floor[indices_between(x1, x2), indices_between(y1, y2)] += 1
    return np.sum(ocean_floor > 1)


def read_input(filename, accept_all=False):
    with open(filename) as f:
        coords = []
        for text_line in f:
            (x1, y1), (x2, y2) = [map(int, pair.split(','))
                                  for pair in text_line.strip().split(' -> ')]
            if x1 == x2 or y1 == y2 or accept_all:
                coords.append((x1, x2, y1, y2))
    return coords


if __name__ == '__main__':
    print('Day 5a:', count_overlaps(read_input("day5/day5.txt")))
    print('Day 5b:', count_overlaps(read_input("day5/day5.txt", accept_all=True)))
