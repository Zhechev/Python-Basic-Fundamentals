def left(count, string):
    result = ''

    for j in range(0, count):
        first_elem = string[0]

        result = string[1:]

        result = result + first_elem
        string = result

    return result


def right(count, string):
    result = ''

    for j in range(0, count):
        last_elem = string[-1]

        result = string[0:-1]

        result = last_elem + result
        string = result

    return result


def insert(index, insert_string, string):
    result = string[:index] + insert_string + string[index:]
    return result


def delete(start_index, end_index, string):
    result = string[:start_index] + string[(end_index+1):]
    return result


input_string = input()

while True:
    input_row = input()

    if input_row == 'end':
        break

    input_parts = input_row.split(' ')
    command = input_parts[0]

    if command == 'Delete':
        input_string = delete(int(input_parts[1]), int(input_parts[2]), input_string)
    elif command == 'Insert':
        input_string = insert(int(input_parts[1]), input_parts[2], input_string)
    elif command == 'Left':
        input_string = left(int(input_parts[1]), input_string)
    elif command == 'Right':
        input_string = right(int(input_parts[1]), input_string)

print(input_string)
print
