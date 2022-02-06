import generate_random


def calculate_sum_list_items(list_items):
    sum = 0
    for x in list_items:
        sum += x
    return sum


def print_calc_sum_list_result():
    my_list = generate_random.generate_list_random(list_max_length=10)
    print(f'List to calc sum of items:\t{my_list}')
    sum_my_list = calculate_sum_list_items(my_list)
    print(f'Sum of list items = {sum_my_list}')