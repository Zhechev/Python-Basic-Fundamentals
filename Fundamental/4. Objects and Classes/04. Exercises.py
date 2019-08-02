class Exercise:
    topic = None
    course_name = None
    judge_contest_ling = None
    problems = None

    def __init__(self, topic, course_name, judge_contest_ling, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_ling = judge_contest_ling
        self.problems = problems

    def __str__(self):
        text = f'Exercises: {self.topic}\nProblems for exercises and homework for the "{self.course_name}" course @ SoftUni.\nCheck your solutions here: {self.judge_contest_ling}\n'
        for i in range(0, len(self.problems)):
            if i != len(self.problems) - 1:
                text += f"{i + 1}. {self.problems[i]}\n"
            else:
                text += f"{i + 1}. {self.problems[i]}"

        return text


exercises = []
input_row = input()

while input_row != 'go go go':
    data = list(input_row.split(' -> '))
    exercise = Exercise(data[0], data[1], data[2], data[3].split(', '))
    exercises.append(exercise)
    input_row = input()

for exercise in exercises:
    print(exercise)
