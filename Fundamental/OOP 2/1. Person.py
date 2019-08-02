class Person:
    name = None
    age = None

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def set_age(self, age):
        if age >= 0:
            self.age = age
        else:
            raise Exception("Age must be positive!")

    def set_name(self, name):
        if len(name) < 3:
            raise Exception("Name's length should not be less than 3 symbols!")
        else:
            self.name = name

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Child(Person):
    def set_age(self, age):
        if 15 > age >= 0:
            self.age = age
        elif age < 0:
            raise Exception("Age must be positive!")
        elif age >= 15:
            raise Exception("Child's age must be less than 15!")

    def set_name(self, name):
        if len(name) < 3:
            raise Exception("Name's length should not be less than 3 symbols!")
        else:
            self.name = name


name = input()
age = int(input())

try:
    person = Child(name, age)
    print(person)
except Exception as e:
    print(e)
