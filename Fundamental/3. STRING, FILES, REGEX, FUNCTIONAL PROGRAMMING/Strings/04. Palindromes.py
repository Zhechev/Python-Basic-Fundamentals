words = input().split(' ')
result = []

for word in words:
    # first solution:
    # part_index = int(len(word)/2)
    # if len(word) % 2 != 0:
    #     left_part = word[0:part_index+1]
    # else:
    #     left_part = word[0:part_index]
    # right_part = ''.join(reversed(word[part_index:]))
    #
    # if (left_part == right_part or len(word) == 1) and word not in result:
    #     result.append(word)

    # second solution:
    if (word == ''.join(reversed(word))) and word not in result:
        result.append(word)

result = sorted(result, key=lambda s: s.lower())

print(', '.join(result))
