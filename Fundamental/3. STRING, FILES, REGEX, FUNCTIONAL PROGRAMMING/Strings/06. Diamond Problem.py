input_string = input()
flag = False

while True:
    left_symbol_index = input_string.find('<')
    right_symbol_index = input_string.find('>')

    if left_symbol_index == -1 or right_symbol_index == -1:
        if flag:
            break
        print(f"Better luck next time")
        break
    else:
        if left_symbol_index > right_symbol_index:
            input_string = input_string.replace('>', '', 1)
        else:
            flag = True
            diamond = input_string[left_symbol_index+1:right_symbol_index]
            test_string = input_string[left_symbol_index:right_symbol_index+1]
            input_string = input_string.replace(test_string, '')
            carats_sum = 0

            for char in diamond:
                if char.isdigit():
                    carats_sum += int(char)

            print(f"Found {carats_sum} carat diamond")
