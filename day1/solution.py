def day1(nums, jump_size):
    return sum(b > a for a, b in zip(nums, nums[jump_size:]))


if __name__ == "__main__":
    my_input = list(map(int, open('day1/input.txt')))
    print(f'Part A: {day1(my_input, jump_size=1)=}')
    print(f'Part B: {day1(my_input, jump_size=3)=}')