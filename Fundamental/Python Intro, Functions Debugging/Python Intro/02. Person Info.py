def print_person_info(name, age, town, salary):
    if isinstance(salary, float):
        print(f'{name} is {age} years old, is from {town} and makes ${float(salary):.2f}')
    else:
        print(f'{name} is {age} years old, is from {town} and makes ${float(salary)}')

name = input()
age = int(input())
town = input()
salary = input()

print_person_info(name, age, town, salary)
