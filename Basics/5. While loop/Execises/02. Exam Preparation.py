num_allowed_poor_grades = int(input())
num_poor_grades = 0
number_of_problems = 0
last_problem = None
sum_grade = 0

task = input()

while task != 'Enough':
    grade = int(input())
    last_problem = task
    if grade <= 4:
        num_poor_grades += 1
    if num_poor_grades == num_allowed_poor_grades:
        print(f'You need a break, {num_poor_grades} poor grades.')
        exit()

    number_of_problems += 1
    sum_grade += grade
    task = input()

avg = sum_grade / number_of_problems
print(f'Average score: {avg:.2f}')
print(f'Number of problems: {number_of_problems}')
print(f'Last problem: {last_problem}')
