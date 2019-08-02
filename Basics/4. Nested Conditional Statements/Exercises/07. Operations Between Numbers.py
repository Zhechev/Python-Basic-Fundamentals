num1 = int(input())
num2 = int(input())
operator = input()

if (operator == '/' or operator == '%') and num2 == 0:
    print(f'Cannot divide {num1} by zero')
    exit()

if operator == '+':
    result = num1 + num2
    even_odd = result % 2 == 0 and 'even' or 'odd'
    print(f'{num1} + {num2} = {result} - {even_odd}')
elif operator == '-':
    result = num1 - num2
    even_odd = result % 2 == 0 and 'even' or 'odd'
    print(f'{num1} - {num2} = {result} - {even_odd}')
elif operator == '*':
    result = num1 * num2
    even_odd = result % 2 == 0 and 'even' or 'odd'
    print(f'{num1} * {num2} = {result} - {even_odd}')
elif operator == '/':
    result = num1 / num2
    print(f'{num1} / {num2} = {result:.2f}')
elif operator == '%':
    result = num1 % num2
    print(f'{num1} % {num2} = {result}')
