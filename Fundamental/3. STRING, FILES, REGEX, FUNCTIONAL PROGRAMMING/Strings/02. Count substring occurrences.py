string = input().lower()
substring = input().lower()
test = ''
count = 0
i = 0

while i < len(string):
    test += string[i]

    if test == substring:
        count += 1
        lenn = len(substring)
        i -= lenn - 2
        test = ''
    else:
        if not substring.startswith(test):
            test = ''
        i += 1

print(count)
