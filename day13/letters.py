import numpy as np

LETTERS = {  # Only including the letters I had in my input
"""
###.
#..#
###.
#..#
#..#
###.
""".strip(): "B",

"""
####
#...
###.
#...
#...
####
""".strip(): "E",

"""
####
#...
###.
#...
#...
#...
""".strip(): "F",

"""
..##
...#
...#
...#
#..#
.##.
""".strip(): "J",

"""
#..#
#.#.
##..
#.#.
#.#.
#..#
""".strip(): "K",

"""
#...
#...
#...
#...
#...
####
""".strip(): "L",

"""
####
...#
..#.
.#..
#...
####
""".strip(): "Z",
}


def visualise_bool_array(array, true_char='#', false_char='.'):
    # Posted as https://stackoverflow.com/a/70358191/493553
    chars = np.empty_like(array, dtype=np.str_)
    chars[array] = true_char
    chars[~array] = false_char
    return np.array2string(chars, separator='', formatter={'all': lambda x: x}).translate(str.maketrans("", "", " []'"))


def bool_array_to_letter(array, true_char='#', false_char='.'):
    return LETTERS[visualise_bool_array(array, true_char, false_char)]


def letter_to_array(letter_representation, true_char='#'):
    char_entries = letter_representation.split()
    bool_entries = [[c == true_char for c in line] for line in char_entries]
    return np.asarray(bool_entries, dtype=bool)


if __name__ == '__main__':
    for letter_representation, letter in LETTERS.items():
        assert bool_array_to_letter(letter_to_array(letter_representation)) == letter
