sequence = input()
dict_result = {}

for letter in sequence:
    letter = letter.lower()
    if letter in dict_result:
        dict_result[letter] += 1
    else:
        dict_result[letter] = 1

for key, value in dict_result.items():
    print(f'{key} -> {value}')
