import random


def calc_sum_digits_number(number, sum_digits=0):
    if number < 10:
        sum_digits += number
        return sum_digits
    return calc_sum_digits_number(number // 10, (number % 10) + sum_digits)


def print_sum_digits_number():
    digits_number = random.randrange(1, 10)
    test_number = random.randrange(10**digits_number)
    sum_digits = calc_sum_digits_number(test_number)
    print(f'Number = {test_number}\nSum of number digits = {sum_digits}')