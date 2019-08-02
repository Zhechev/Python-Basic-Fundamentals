class Point:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Box:
    upper_left = None
    upper_right = None
    bottom_left = None
    bottom_right = None

    def __init__(self, upper_left, upper_right, bottom_left, bottom_right):
        self.upper_left = upper_left
        self.upper_right = upper_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

    def get_width(self):
        return abs(int(self.upper_right.x) - int(self.upper_left.x))

    def get_height(self):
        return abs(int(self.bottom_left.y) - int(self.upper_left.y))

    def calculate_perimeter(self):
        return 2 * self.get_height() + 2 * self.get_width()

    def calculate_area(self):
        return self.get_height() * self.get_width()

    def __str__(self):
        return f'Box: {self.get_width()}, {self.get_height()}\nPerimeter: {self.calculate_perimeter()}\nArea: {self.calculate_area()}'


boxes_list = []
while True:
    data = input()

    if data == 'end':
        break

    data = data.split(' | ')

    upper_left = Point(data[0].split(':')[0], data[0].split(':')[1])
    upper_right = Point(data[1].split(':')[0], data[1].split(':')[1])
    bottom_left = Point(data[2].split(':')[0], data[2].split(':')[1])
    bottom_right = Point(data[3].split(':')[0], data[3].split(':')[1])

    box = Box(upper_left, upper_right, bottom_left, bottom_right)
    boxes_list.append(box)

for box in boxes_list:
    print(box)
