import math
figure = input()

if figure == 'square':
    side = float(input())
    print("%.3f" % (math.pow(side, 2)))
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    print("%.3f" % (a * b))
elif figure == 'circle':
    r = float(input())
    print("%.3f" % (math.pi * math.pow(r, 2)))
elif figure == 'triangle':
    side = float(input())
    h = float(input())
    print("%.3f" % ((side * h) / 2))
