def day2a(commands):
    depth = 0
    horizontal = 0
    for direction, amount in commands:
        if direction == "forward":
            horizontal += amount
        elif direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount
    return depth * horizontal


def day2b(commands):
    aim = 0
    depth = 0
    horizontal = 0
    for direction, amount in commands:
        if direction == "forward":
            horizontal += amount
            depth += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
    return depth * horizontal


if __name__ == "__main__":
    my_input = [(s[0], int(s[1])) for s in map(str.split, open('day2/day2.txt'))]
    print(f'Day 2a: {day2a(my_input)}')
    print(f'Day 2b: {day2b(my_input)}')