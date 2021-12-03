def bits_to_rate(bits):
    return int(''.join(map(str, bits)), 2)


def bit_sum_to_common_bit(bit_sum, length, round_up=False):
    return int(bit_sum * 2 > length or round_up and bit_sum * 2 == length)


def day3a(input_strings):
    digit_sums = (sum(map(int, digit_i)) for digit_i in zip(*input_strings))
    common_bits = [bit_sum_to_common_bit(bit_sum, len(input_strings)) for bit_sum in digit_sums]

    gamma_rate = bits_to_rate(common_bits)
    epsilon_rate = bits_to_rate(1-bit for bit in common_bits)
    return gamma_rate * epsilon_rate


def filter_has_most_common_bit_in_pos(nums, pos):
    bit_sum = sum(int(num[pos]) for num in nums)
    common_bit = bit_sum_to_common_bit(bit_sum, len(nums), round_up=True)
    return {num for num in nums if int(num[pos]) == common_bit}


def filter_has_least_common_bit_in_pos(nums, pos):
    bit_sum = sum(int(num[pos]) for num in nums)
    least_common_bit = 1 - bit_sum_to_common_bit(bit_sum, len(nums), round_up=True)
    return {num for num in nums if int(num[pos]) == least_common_bit}


def filter_last_one_standing(nums, filter_func):
    valid_nums = set(nums)
    for pos in range(len(nums)):
        valid_nums = filter_func(valid_nums, pos)
        if len(valid_nums) == 1:
            return bits_to_rate(valid_nums.pop())
    raise RuntimeError("The amount of valid nums in the following set is not 1: {valid_nums}")


def day3b(input_strings):
    oxygen_generator = filter_last_one_standing(input_strings, filter_has_most_common_bit_in_pos)
    co2_scrubber = filter_last_one_standing(input_strings, filter_has_least_common_bit_in_pos)
    return oxygen_generator * co2_scrubber


my_input = list(map(str.strip, open('day3.txt')))
print(day3a(my_input))
print(day3b(my_input))