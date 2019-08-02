def is_inside(r1, r2):
    if r1.left >= r2.left and r1.right <= r2.right and r1.top <= r2.top and r1.bottom <= r2.bottom:
        return True


class Rectangle:
    def __init__(self, left, top, width, height):
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.set_right()
        self.set_bottom()

    def set_right(self):
        self.right = self.left + self.width

    def set_bottom(self):
        self.bottom = self.top + self.height


r1 = list(map(float, input().split(' ')))
r2 = list(map(float, input().split(' ')))

r1 = Rectangle(r1[0], r1[1], r1[2], r1[3])
r2 = Rectangle(r2[0], r2[1], r2[2], r2[3])

if is_inside(r1, r2):
    print("Inside")
else:
    print("Not inside")
