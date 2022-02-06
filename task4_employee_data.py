def print_employee_data(name, salary=9000):
    if salary < 0:
        salary = 0
    print(f'Name = {name}\nSalary = {salary}')