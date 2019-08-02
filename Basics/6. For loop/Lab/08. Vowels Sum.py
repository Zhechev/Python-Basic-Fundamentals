s = input()
sum = 0

for i in range(0, s.__len__()):
    if s[i] == 'a':
        sum += 1
    elif s[i] == 'e':
        sum += 2
    elif s[i] == 'i':
        sum += 3
    elif s[i] == 'o':
        sum += 4
    elif s[i] == 'u':
        sum += 5

print(sum)
