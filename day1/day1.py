def day1(nums, jump_size):
    return sum(b > a for a, b in zip(nums, nums[jump_size:]))


if __name__ == "__main__":
    my_input = list(map(int, open('day1/day1.txt')))
    print(f'Day 1a: {day1(my_input, jump_size=1)=}')
    print(f'Day 1b: {day1(my_input, jump_size=3)=}')