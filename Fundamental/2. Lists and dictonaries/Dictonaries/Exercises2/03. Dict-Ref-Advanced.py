result = {}

while True:
    input_row = input()

    if input_row == 'end':
        break

    input_parts = input_row.split(' -> ')
    key = input_parts[0]
    value = input_parts[1]

    if key in result:
        result[key] = result[key] + ', ' + value
    elif value in result:
        result[key] = result[value]
    elif value not in result and not value.isalpha():
        result[key] = value

for key, value in result.items():
    print(f"{key} === {value}")
