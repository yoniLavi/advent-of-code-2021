from statistics import median


CHUNK_PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}
CHUNK_PENALTY = {")": 3, "]": 57, "}": 1197, ">": 25137}
CHUNK_SCORE = {"(": 1, "[": 2, "{": 3, "<": 4}


def line_penalty(line):
    stack = []
    for chunk in line:
        if chunk in CHUNK_PAIRS:
            stack.append(chunk)
        elif not stack or CHUNK_PAIRS[stack.pop()] != chunk:
            return CHUNK_PENALTY[chunk], None
    return 0, stack


def day10a(lines):
    return sum(line_penalty(l)[0] for l in lines)


def incompleteness_score(stack):
    score = 0
    for chunk in reversed(stack):
        score = score * 5 + CHUNK_SCORE[chunk]
    return score


def day10b(lines):
    incomplete_stacks = [stack for score, stack in map(line_penalty, lines) if stack]
    return median(map(incompleteness_score, incomplete_stacks))


if __name__ == "__main__":
    lines = [line.strip() for line in open('day10/input.txt')]
    print(f'Part A: {day10a(lines)}')
    print(f'Part B: {day10b(lines)}')
