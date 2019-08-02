while True:
    first_row = input()

    if first_row == 'collapse':
        break

    second_row = input()

    while len(second_row) > 0:
        if second_row in first_row:
            first_row = first_row.replace(second_row, "")

        second_row = second_row[1:-1]

    if not first_row:
        print("(void)")
    else:
        print(first_row)
