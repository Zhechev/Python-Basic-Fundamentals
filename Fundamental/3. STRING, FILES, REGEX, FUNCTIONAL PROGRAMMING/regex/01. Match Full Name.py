import re

names = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+"

matches = re.findall(pattern, names)

for match in matches:
    print(match, end=" ")
