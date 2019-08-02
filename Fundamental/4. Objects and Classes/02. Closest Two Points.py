import math


def calculate_distance(first_point, second_point):
    side_a = first_point.x - second_point.x
    side_b = first_point.y - second_point.y
    result = math.sqrt(side_a**2 + side_b**2)

    return result


class Point:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


class PointsDistance:
    first_point = None
    second_point = None
    distance = None

    def __init__(self, first_point, second_point, distance):
        self.first_point = first_point
        self.second_point = second_point
        self.distance = distance


n = int(input())
points = []

while n > 0:
    point = list(map(float, input().split()))
    point = Point(point[0], point[1])
    points.append(point)

    n -= 1

distances = []
for index_fp in range(0, len(points)):
    for index_sp in range(0, len(points)):
        if index_fp != index_sp:
            distance = calculate_distance(points[index_fp], points[index_sp])
            distance_points = PointsDistance(points[index_fp], points[index_sp], distance)
            distances.append(distance_points)

min_distance = sorted(distances, key=lambda distance_points: distance_points.distance)[0]
print(f'{min_distance.distance:.3f}')
print(f'({int(min_distance.first_point.x)}, {int(min_distance.first_point.y)})')
print(f'({int(min_distance.second_point.x)}, {int(min_distance.second_point.y)})')

