import re

numbers = input()
pattern = r"\b(0x)?[0-9A-F]+\b"
matches = re.finditer(pattern, numbers)


for match in matches:
    print(f"{match.group()}", end=" ")
