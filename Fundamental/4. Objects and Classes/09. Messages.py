from itertools import zip_longest


class User:
    username = None
    received_messages = None

    def __init__(self, username):
        self.username = username
        self.received_messages = []


class Message:
    content = None
    sender = None

    def __init__(self, sender, content):
        self.content = content
        self.sender = sender


input_row = input()
users = {}

while input_row != 'exit':
    data = input_row.split(' ')

    if data[0] == 'register':
        username = data[1]
        user = User(username)
        users[username] = user
    else:
        sender_username = data[0]
        recipient_username = data[2]
        content = data[3]
        if recipient_username in users and sender_username in users:
            message = Message(sender_username, content)
            users[recipient_username].received_messages.append(message)

    input_row = input()

final_users = input().split(' ')
first_user = final_users[0]
second_user = final_users[1]
flag = True

for l1, l2 in zip_longest(users[first_user].received_messages, users[second_user].received_messages, fillvalue=''):
    if l2 and (l2.sender == first_user or l2.sender == second_user):
        flag = False
        print(f"{first_user}: {l2.content}")
    if l1 and (l1.sender == first_user or l1.sender == second_user):
        flag = False
        print(f"{l1.content} :{second_user}")

if flag:
    print("No messages")
