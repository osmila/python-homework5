import generate_random


def multiply_list_items(list_param, res=1):
    if len(list_param) == 0:
        return res
    else:
        res *= list_param[0]
        list_param.pop(0)
        return multiply_list_items(list_param, res)


def print_res_multiply_list_items():
    my_list = generate_random.generate_list_random(list_max_length=10)
    print(f'Initial list is:\t{my_list}')
    result = multiply_list_items(my_list)
    print(f'Multiplication result is:\t{result}')