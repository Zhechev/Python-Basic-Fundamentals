class Dog:
    name = None
    age = None
    number_of_legs = None

    def __init__(self, name, age, number_of_legs):
        self.name = name
        self.age = age
        self.number_of_legs = number_of_legs

    def produce_sound(self):
        print("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")


class Cat:
    name = None
    age = None
    intelligence_quotient = None

    def __init__(self, name, age, intelligence_quotient):
        self.name = name
        self.age = age
        self.intelligence_quotient = intelligence_quotient

    def produce_sound(self):
        print("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")


class Snake:
    name = None
    age = None
    cruelty_coefficient = None

    def __init__(self, name, age, cruelty_coefficient):
        self.name = name
        self.age = age
        self.cruelty_coefficient = cruelty_coefficient

    def produce_sound(self):
        print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")


input_row = input()
dogs = {}
cats = {}
snakes = {}

while input_row != "I\'m your Huckleberry":
    data = input_row.split(' ')
    class_or_talk = data[0]

    if class_or_talk == 'talk':
        name = data[1]
        if name in dogs:
            animal = dogs[name]
        elif name in cats:
            animal = cats[name]
        else:
            animal = snakes[name]
        animal.produce_sound()

    else:
        name = data[1]
        age = data[2]
        parameter = data[3]

        if class_or_talk == 'Dog':
            animal = Dog(name, age, parameter)
            dogs[animal.name] = animal
        elif class_or_talk == 'Cat':
            animal = Cat(name, age, parameter)
            cats[animal.name] = animal
        else:
            animal = Snake(name, age, parameter)
            snakes[animal.name] = animal

    input_row = input()

for dog in dogs:
    dog = dogs[dog]
    print(f"Dog: {dog.name}, Age: {dog.age}, Number Of Legs: {dog.number_of_legs}")
for cat in cats:
    cat = cats[cat]
    print(f"Cat: {cat.name}, Age: {cat.age}, IQ: {cat.intelligence_quotient}")
for snake in snakes:
    snake = snakes[snake]
    print(f"Snake: {snake.name}, Age: {snake.age}, Cruelty: {snake.cruelty_coefficient}")

