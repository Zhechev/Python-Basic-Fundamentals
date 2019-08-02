import math

l = float(input())
w = float(input())
a = float(input())

roomSize = (l * 100) * (w * 100)
wardrobeSize = (a * 100) * (a * 100)
benchSize = roomSize / 10
freeSpace = roomSize - wardrobeSize - benchSize
numberDancers = freeSpace / (40 + 7000)
print(math.floor(numberDancers))
