def bits_to_decimal(bits):
    return int(''.join(map(str, bits)), 2)


def most_common_bit_in_pos(nums, pos):
    bit_sum = sum(int(num[pos]) for num in nums)
    return int(2 * bit_sum >= len(nums))


def least_common_bit_in_pos(nums, pos):
    return 1 - most_common_bit_in_pos(nums, pos)


def day3a(nums):
    gamma_rate = bits_to_decimal(most_common_bit_in_pos(nums, pos) for pos in range(len(nums[0])))
    epsilon_rate = bits_to_decimal(least_common_bit_in_pos(nums, pos) for pos in range(len(nums[0])))
    return gamma_rate * epsilon_rate


def filter_last_one_standing(valid_nums, criterion_func, pos=0):
    if len(valid_nums) == 1:
        return bits_to_decimal(valid_nums[0])

    criterion_bit = criterion_func(valid_nums, pos)
    filtered_nums = [num for num in valid_nums if int(num[pos]) == criterion_bit]
    return filter_last_one_standing(filtered_nums, criterion_func, pos + 1)


def day3b(input_strings):
    oxygen_generator = filter_last_one_standing(input_strings, most_common_bit_in_pos)
    co2_scrubber = filter_last_one_standing(input_strings, least_common_bit_in_pos)
    return oxygen_generator * co2_scrubber


if __name__ == '__main__':
    my_input = list(map(str.strip, open('day3/day3.txt')))
    print(f'Day 3a: {day3a(my_input)}')
    print(f'Day 3b: {day3b(my_input)}')