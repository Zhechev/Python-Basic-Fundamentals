x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x = abs(x1 - x2)
y = abs(y1 - y2)

area = x * y
perimeter = 2 * (x + y)

print("%.2f" % abs(area))
print("%.2f" % abs(perimeter))
