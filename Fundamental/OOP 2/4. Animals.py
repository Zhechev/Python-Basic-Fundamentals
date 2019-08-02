from abc import ABC, abstractmethod


class Animal(ABC):
    name = None
    age = None
    gender = None

    def __init__(self, name, age, gender):
        self.set_name(name)
        self.set_age(age)
        self.set_gender(gender)

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        if age < 0:
            raise Exception("Invalid input!")
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    @abstractmethod
    def produce_sound(self):
        pass

    def __str__(self):
        return f"{type(self).__name__}\n{self.name} {self.age} {self.gender}"


class Dog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return("Woof!")


class Frog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return("Ribbit")


class Cat(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return("Meow meow")


class Kitten(Cat):
    def __init__(self, name, age, gender):
        Cat.__init__(self, name, age, gender)

    def set_gender(self, gender):
        self.gender = 'Female'

    def produce_sound(self):
        return("Meow")


class Tomcat(Cat):
    def __init__(self, name, age, gender):
        Cat.__init__(self, name, age, gender)

    def set_gender(self, gender):
        self.gender = 'Male'

    def produce_sound(self):
        return("MEOW")


animals = []
animals_types = ['Dog', 'Cat', 'Frog', 'Kitten', 'Tomcat']
while True:
    row = input()

    if row == 'Beast!':
        break

    name, age, gender = input().split()

    if row not in animals_types:
        print("Invalid input!")
    else:
        string = f'{row}("{name}", {age}, "{gender}")'
        try:
            animal = eval(string)
            animals.append(animal)
        except Exception as e:
            print(e)

for animal in animals:
    print(animal)
    print(animal.produce_sound())
