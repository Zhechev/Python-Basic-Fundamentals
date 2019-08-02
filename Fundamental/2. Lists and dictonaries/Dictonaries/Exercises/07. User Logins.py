users_dict = {}
unsuccessfull_login_attempts_count = 0

while True:
    command = input()

    if command == 'login':
        break

    username_parts = command.split(' -> ')
    username = username_parts[0]
    user_pass = username_parts[1]

    users_dict[username] = user_pass

while True:
    command = input()

    if command == 'end':
        break

    username_parts = command.split(' -> ')
    username = username_parts[0]
    user_pass = username_parts[1]

    if username not in users_dict or users_dict[username] != user_pass:
        print(f'{username}: login failed')
        unsuccessfull_login_attempts_count += 1
    else:
        print(f'{username}: logged in successfully')

print(f'unsuccessful login attempts: {unsuccessfull_login_attempts_count}')
