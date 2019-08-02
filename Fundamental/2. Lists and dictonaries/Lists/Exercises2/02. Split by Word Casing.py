import re

list_lower_case = []
list_upper_case = []
list_mixed_case = []

input_words = list(re.split('[\s,;:.!()"\'\\\/\[\]]', input()))
str_list = list(filter(None, input_words))

for i in str_list:
    if i.islower() and i.isalpha():
        list_lower_case.append(i)
    elif i.isupper() and i.isalpha():
        list_upper_case.append(i)
    else:
        list_mixed_case.append(i)

print(f"Lower-case: {', '.join(list_lower_case)}")
print(f"Mixed-case: {', '.join(list_mixed_case)}")
print(f"Upper-case: {', '.join(list_upper_case)}")
