import numpy as np

from letters import bool_array_to_letter


def input_pairs_to_matrix(paper_pairs):
    size = tuple(map(lambda values: max(values) + 1, zip(*paper_pairs)))[::-1]
    paper = np.zeros(size, dtype=bool)
    paper[tuple(zip(*paper_pairs))[::-1]] = True
    return paper


def parse_input(filename):
    pairs = []
    dimensions = []
    with open(filename) as f:
        for line in f:
            if not line.strip():
                break
            pairs.append(tuple(map(int, line.split(','))))
        for line in f:
            dimensions.append(line.strip().split()[-1].split('='))
    return input_pairs_to_matrix(pairs), [dim for dim, _ in dimensions]


def fold_x(paper):
    value = paper.shape[1] // 2
    folded_paper = np.zeros((paper.shape[0], value), dtype=bool)
    folded_paper[:, :] = paper[:, :value]
    folded_paper |= np.fliplr(paper[:, value+1:])
    return folded_paper


def fold_once(paper, dim):
    return fold_x(paper.T).T if dim == 'y' else fold_x(paper)


def day13a(paper, dim):
    return fold_once(paper, dim).sum()


def day13b(paper, fold_dimensions):
    for dim in fold_dimensions:
        paper = fold_once(paper, dim)
    
    letters = []
    for letter_start_col in range(0, paper.shape[1], 5):
        letter_bool_array = paper[:, letter_start_col:letter_start_col+4].copy()
        letters.append(bool_array_to_letter(letter_bool_array))
    return ''.join(letters)


if __name__ == '__main__':
    paper, fold_dimensions = parse_input('day13/input.txt')
    print(f'Part A: {day13a(paper, fold_dimensions[0])}')
    print(f'Part B: {day13b(paper, fold_dimensions)}')
