hours = int(input())
minutes = int(input())

minutes += 15

if minutes > 59:
    minutes -= 60
    hours += 1

if hours > 23:
    hours -= 24

result = str(hours) + ':' + (str(minutes) if minutes >= 10 else '0' + str(minutes))
print(result)
