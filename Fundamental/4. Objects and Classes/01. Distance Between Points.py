import math


def cald_distance(first_point, second_point):
    side_a = abs(first_point.x - second_point.x)
    side_b = abs(first_point.y - second_point.y)
    side_c = math.sqrt(side_a**2 + side_b**2)
    return  side_c




class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


first_point = list(map(float, input().split()))
first_point = Point(first_point[0], first_point[1])
second_point = list(map(float, input().split()))
second_point = Point(second_point[0], second_point[1])

distance = cald_distance(first_point, second_point)

print(f"{distance:.3f}")


