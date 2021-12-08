def parse_entry(line):
    return [list(map(frozenset, digits.split()))
            for digits in line.strip().split(' | ')]


def day8a(entries):
    return sum(len(digits) in [2, 3, 4, 7]
               for entry in entries
               for digits in entry[1])


def disambiguate_235(two_three_five, four):
    two = next(digit for digit in two_three_five if len(digit & four) == 2)
    three = next(digit for digit in two_three_five if len(digit & two) == 4)
    five = next(iter(two_three_five - {two, three}))
    return two, three, five


def disambiguate_069(zero_six_nine, one, four):
    nine = next(digit for digit in zero_six_nine if len(digit & four) == 4)
    six = next(digit for digit in zero_six_nine if len(digit & one) == 1)
    zero = next(iter(zero_six_nine - {nine, six}))
    return zero, six, nine


def decipher_entry(entry):
    digits, output_number = entry
    one = next(digit for digit in digits if len(digit) == 2)
    four = next(digit for digit in digits if len(digit) == 4)
    seven = next(digit for digit in digits if len(digit) == 3)
    eight = next(digit for digit in digits if len(digit) == 7)

    two_three_five = frozenset(digit for digit in digits if len(digit) == 5)
    zero_six_nine = frozenset(digit for digit in digits if len(digit) == 6)
    two, three, five = disambiguate_235(two_three_five, four)
    zero, six, nine = disambiguate_069(zero_six_nine, one, four)

    known_digits = [zero, one, two, three, four, five, six, seven, eight, nine]
    digit_getter = {digit: str(position) for position, digit in enumerate(known_digits)}
    return int(''.join(map(digit_getter.get, output_number)))


def day8b(entries):
    return sum(map(decipher_entry, entries))


if __name__ == '__main__':
    my_input = list(map(parse_entry, open('day8/input.txt')))
    print(f'Part A: {day8a(my_input)}')
    print(f'Part B: {day8b(my_input)}')
