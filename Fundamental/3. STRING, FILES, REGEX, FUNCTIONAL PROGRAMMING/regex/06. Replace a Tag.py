import re
result = []

while True:

    input_row = input()

    if input_row == 'end':
        break

    result.append(input_row)

pattern_begin = r"<a ?"
pattern_middle = r"[^s|.|>|a|ul|li]>"
pattern_end = "</a>"

for i in range(0, len(result)):
    result[i] = re.sub(pattern_begin, '[URL ', result[i])
    result[i] = re.sub(pattern_end, '[/URL]', result[i])
    result[i] = re.sub(pattern_middle, '"]', result[i])

for line in result:
    print(f"{line}")
