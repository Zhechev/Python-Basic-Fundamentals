jury_num = int(input())
presentation_name = input()
all_presentations_grade = 0
grades_count = 0

while presentation_name != 'Finish':
    avg_current_presentation_grade = 0
    current_presentation_grade = 0

    for i in range(0, jury_num):
        grade = float(input())
        grades_count += 1
        current_presentation_grade += grade
    avg_current_presentation_grade = current_presentation_grade / jury_num
    print(f'{presentation_name} - {avg_current_presentation_grade:.2f}.')

    all_presentations_grade += current_presentation_grade

    presentation_name = input()

avg_all_presentations_grade = all_presentations_grade / grades_count
print(f'Student\'s final assessment is {avg_all_presentations_grade:.2f}.')
