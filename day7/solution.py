from statistics import mean, median


def day7a(nums):
    optimal_pos = round(median(nums))
    return sum(abs(n-optimal_pos) for n in nums)


def partb_total_fuel(target_pos, nums):
    def fuel_func(n):
        dist = abs(n-target_pos)
        return dist * (dist + 1) // 2
    return sum(map(fuel_func, nums))


def day7b(nums):
    mean_pos = round(mean(nums))
    # I couldn't quite figure out the optimal statistic to minimise this cost
    # function, but it's clearly close to the mean, so just searching around it
    return min(partb_total_fuel(pos, nums)
               for pos in range(mean_pos-5, mean_pos+5))


if __name__ == '__main__':
    my_input = list(map(int, open('day7/input.txt').read().strip().split(',')))
    print(f'Part A: {day7a(my_input)}')
    print(f'Part B: {day7b(my_input)}')
