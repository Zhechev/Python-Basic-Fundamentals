num = int(input())
num_length = str(num).__len__()

for i in range(0, num_length):
    last_digit = int(num % 10)

    if last_digit == 0:
        print('ZERO')
    else:
        print(chr(last_digit + 33)*last_digit)
    num /= 10
