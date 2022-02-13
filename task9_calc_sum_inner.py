import random

def outer_calc_sum(a, b):
    sum = 0
    def inner_calc_sum():
        return a + b
    sum += inner_calc_sum()
    sum += 5
    return sum


def print_sum_outer_inner():
    a = random.randrange(1, 10)
    b = random.randrange(1, 10)
    print(f'a = {a}\nb = {b}')
    sum = outer_calc_sum(a, b)
    print(f'sum = {sum}')
