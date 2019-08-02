dict_employers_age= {}
dict_employers_salary = {}
dict_employers_position = {}


while True:
    command = input()
    if command == 'filter base':
        break

    employee_parts = command.split(' -> ')
    employee_name = employee_parts[0]
    employee_param = employee_parts[1]
    try:
        employee_param = int(employee_param)
        dict_employers_age[employee_name] = employee_param
        continue
    except ValueError:
        pass
    try:
        employee_param = float(employee_param)
        dict_employers_salary[employee_name] = employee_param
        continue
    except ValueError:
        pass
    try:
        employee_param = str(employee_param)
        dict_employers_position[employee_name] = employee_param
        continue
    except ValueError:
        pass

filter = input()

if filter == 'Age':
    for key, value in dict_employers_age.items():
        print(f'Name: {key}')
        print(f'Age: {value}')
        print(f'====================')
elif filter == 'Salary':
    for key, value in dict_employers_salary.items():
        print(f'Name: {key}')
        print(f'Salary: {value}')
        print(f'====================')
else:
    for key, value in dict_employers_position.items():
        print(f'Name: {key}')
        print(f'Position: {value}')
        print(f'====================')
