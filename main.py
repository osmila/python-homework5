import random
import task1_calc_sum_diff
import task2_calc_sum_list_items
import task3_variable_length_args
import task4_employee_data
import task5_sum_digits_of_number
import task6_fibonacci_number
import task7_multiply_list_items
import task8_power_of_two
import task9_calc_sum_inner

# Task 1:
# Напишите функцию calculations () так, чтобы она могла
# принимать две переменные и вычислять их сложение и
# вычитание. А также он должен возвращать как сложение, так
# и вычитание за один вызов возврата.
print('Task 1: Calculate sum and diff of 2 random values:')
test_value_1 = random.randrange(10)
test_value_2 = random.randrange(10)
print(f'Value 1 = {test_value_1}, value 2 = {test_value_2}')
sum_test, diff_test = task1_calc_sum_diff.calculations(test_value_1, test_value_2)
print(f'Sum = {sum_test}\nDiff = {diff_test}')

# Task 2:
# Напишите функцию Python для суммирования всех чисел в списке.
print('\nTask 2: Calculate sum of list items:')
task2_calc_sum_list_items.print_calc_sum_list_result()

# Task 3:
# Напишите функцию func () так, чтобы она могла принимать
# аргументы переменной длины и выводить все значения
# аргументов с индексом аргумента.
print('\nTask 3: Print arguments from the list with indexes:')
task3_variable_length_args.variable_length_func(5, 6, 7, 'Hello')

# Task 4:
# Создайте функцию showEmployee () таким образом, чтобы она
# принимала имя сотрудника и его зарплату и отображала и то, и
# другое. Если в вызове функции отсутствует зарплата, присвойте
# зарплате значение по умолчанию 9000.
print('\nTask 4: Print employee name and salary:')
task4_employee_data.print_employee_data(name='Petro', salary=5000)
task4_employee_data.print_employee_data(name='Ivan')

# Task 5:
# Дано натуральное число N. Вычислите сумму его цифр.
# Напишите рекурсивную функцию
print('\nTask 5: Sum digits of the natural number:')
task5_sum_digits_of_number.print_sum_digits_number()

# Task 6:
# Напишите рекурсивную функцию для вычисления числа Фибоначи
print('\nTask 6: Calculate Fibonacci number:')
task6_fibonacci_number.print_fibonacci_value()

# Task 7:
# Напишите функцию для умножения всех чисел в списке. Рекурсивно
print('\nTask 7: Multiply list items:')
task7_multiply_list_items.print_res_multiply_list_items()

# Task 8:
# Дано натуральное число N. Выведите слово YES, если число N
# является точной степенью двойки, или слово NO в противном случае. 8
# - YES, 3 - NO
print('\nTask 8: Check if current value is a power of 2:')
task8_power_of_two.print_power_of_two()

# Task 9:
# Создайте inner функцию для вычисления сложения следующим образом:
# a. Создайте внешнюю функцию, которая будет принимать два параметра, a и b
# b. Создайте внутреннюю функцию внутри внешней функции, которая будет вычислять сложение a и b
# c. Наконец, внешняя функция добавит 5 и вернет ее.
print('\nTask 9: Calculate sum of 2 numbers in the inner func and add 5 in the outer func:')
task9_calc_sum_inner.print_sum_outer_inner()