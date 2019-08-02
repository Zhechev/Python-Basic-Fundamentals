class Human:
    first_name = None
    last_name = None

    def __init__(self, first_name, last_name):
        self.set_first_name(first_name)
        self.set_last_name(last_name)

    def set_first_name(self, first_name):
        if not first_name[0].isupper():
            raise Exception("Expected upper case letter! Argument: firstName")
        elif len(first_name) <= 3:
            raise Exception("Expected length at least 4 symbols! Argument: firstName")
        self.first_name = first_name

    def set_last_name(self, last_name):
        if not last_name[0].isupper():
            raise Exception("Expected upper case letter! Argument: lastName")
        elif len(last_name) <= 3:
            raise Exception("Expected length at least 3 symbols! Argument: lastName")
        self.last_name = last_name


class Student(Human):
    faculty_number = None

    def __init__(self, first_name, last_name, faculty_number):
        Human.__init__(self, first_name, last_name)
        self.set_faculty_number(faculty_number)

    def set_faculty_number(self, faculty_number):
        if len(faculty_number) > 10 or len(faculty_number) < 5:
            raise Exception("Invalid faculty number!");
        self.faculty_number = faculty_number

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nFaculty number: {self.faculty_number}"


class Worker(Human):
    week_salary = None
    work_hours_per_day = None

    def __init__(self, first_name, last_name, week_salary, work_hours_per_day):
        Human.__init__(self, first_name, last_name)
        self.set_week_salary(week_salary)
        self.set_work_hours_per_day(work_hours_per_day)

    def set_week_salary(self, week_salary):
        if week_salary < 10:
            raise Exception("Expected value mismatch! Argument: weekSalary")
        self.week_salary = week_salary

    def set_work_hours_per_day(self, work_hours_per_day):
        if 12 < work_hours_per_day < 1:
            raise Exception("Expected value mismatch! Argument: workHoursPerDay")
        self.work_hours_per_day = work_hours_per_day

    def calculate_salary_per_hour(self):
        return self.week_salary / (self.work_hours_per_day * 5)

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nWeek Salary: {self.week_salary:.2f}\nHours per day: {self.work_hours_per_day:.2f}\nSalary per hour: {self.calculate_salary_per_hour():.2f}"


student_fname, student_lname, student_fnumber = input().split()

worker_parts = input().split()
worker_fname = worker_parts[0]
worker_lname = worker_parts[1]
worker_week_salary = float(worker_parts[2])
worker_work_hours_per_day = float(worker_parts[3])

try:
    student = Student(student_fname, student_lname, student_fnumber)
    worker = Worker(worker_fname, worker_lname, worker_week_salary, worker_work_hours_per_day)
    print(student)
    print()
    print(worker)
except Exception as e:
    print(e)
