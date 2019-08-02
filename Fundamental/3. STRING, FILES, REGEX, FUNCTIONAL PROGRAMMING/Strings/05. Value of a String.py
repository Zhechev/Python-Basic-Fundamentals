text = input()
filter = input()
count = 0

for char in text:
    if filter == 'LOWERCASE':
        if char.islower():
            count += ord(char)
    else:
        if char.isupper():
            count += ord(char)

print(f"The total sum is: {count}")
