result = {}

while True:
    input_row = input()

    if input_row == 'ready':
        break

    input_parts = input_row.split(':')
    city = input_parts[0]
    type_capacity_parts = input_parts[1].split(',')

    for val in type_capacity_parts:
        val = val.split('-')
        if city in result:
            result[city][val[0]] = val[1]
        else:
            result[city] = {val[0]: val[1]}

for key, value in result.items():
    sum = 0
    for k, v in value.items():
        sum += int(v)
    result[key] = sum

while True:
    input_row = input()

    if input_row == 'travel time!':
        break

    input_parts = input_row.split(' ')
    city_travel = input_parts[0]
    people_count = int(input_parts[1])

    if city_travel in result:
        if result[city_travel] > people_count:
            print(f"{city_travel} -> all {people_count} accommodated")
        else:
            print(f"{city_travel} -> all except {people_count - result[city_travel]} accommodated")
