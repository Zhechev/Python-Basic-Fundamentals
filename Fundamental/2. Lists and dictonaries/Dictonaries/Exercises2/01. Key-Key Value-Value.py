searched_key = input()
searched_value = input()
n = int(input())

while n > 0:

    key_value_row = input().split(' => ')
    key = key_value_row[0]
    values = list(key_value_row[1].split(';'))

    if searched_key in key:
        print(f"{key}:")
        for val in values:
            if searched_value in val:
                print(f"-{val}")

    n -= 1

