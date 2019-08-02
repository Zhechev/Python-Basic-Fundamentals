import re

row = input()

pattern = r"([1]?[0-9AJKQ])([SHDC])"

result = ''

for (first, second) in re.findall(pattern, row):
    if first and second:
        if first.isdigit() and int(first) <= 10:
            result += first + second + ' '
        elif first == "J" or first == "Q" or first == "K" or first == "A":
            result += first + second + ' '

print(result)
