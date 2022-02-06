import random


def generate_list_random(list_min_length=1, list_max_length=20):
    length = random.randrange(list_min_length, list_max_length)
    my_list = list()
    for _ in range(length):
        my_list.append(random.randrange(1, 10))
    return my_list
