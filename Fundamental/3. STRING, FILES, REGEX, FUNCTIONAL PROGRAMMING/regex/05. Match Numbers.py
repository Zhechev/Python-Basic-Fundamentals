import re

numbers = input()
pattern = r"(^|(?<=\s))-?\d+\.?\d+($|(?=\s))"
matches = re.finditer(pattern, numbers)


for match in matches:
    print(match.group(), end=" ")
