def simulate(input_ages, simulation_days):
    timers = [0] * 9
    for age in input_ages:
        timers[age] += 1

    for _ in range(simulation_days):
        timers = timers[1:] + [timers[0]]
        timers[6] += timers[8]

    return sum(timers)


if __name__ == '__main__':
    my_input = list(map(int, open('day6/input.txt').read().strip().split(',')))
    print(f'Part A: {simulate(my_input, 80)}')
    print(f'Part B: {simulate(my_input, 256)}')
