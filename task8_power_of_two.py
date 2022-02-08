import random


def is_power_of_two(num):
    if num == 1:
        return True
    elif num < 1:
        return False
    else:
        return is_power_of_two(num / 2)


def print_power_of_two():
    number = random.randrange(1, 1000)
    if number % 2 != 0 or not is_power_of_two(number):
        print(f'Number {number} is NOT a power of 2')
    else:
        print(f'Number {number} is a power of 2')