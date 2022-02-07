import random


def calculate_fibonacci_value(position):
    if position == 1:
        return 1
    elif position == 2:
        return 1
    else:
        return calculate_fibonacci_value(position-1) + calculate_fibonacci_value(position-2)


def print_fibonacci_value():
    rand_position = random.randrange(1, 30)
    fibo_number = calculate_fibonacci_value(rand_position)
    print(f'Fibonacci number at position = {rand_position} will be:\n{fibo_number}')
