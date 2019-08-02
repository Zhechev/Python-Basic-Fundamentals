def compare_ints(num1, num2):
    print(max(num1, num2))


def compare_chars(char1, char2):
    print(chr(max(ord(char1), ord(char2))))


def compare_string(string1, string2):
    print(max(string1, string2))


values = input()

if values == 'int':
    value1 = int(input())
    value2 = int(input())
    compare_ints(value1, value2)
elif values == 'char':
    value1 = input()
    value2 = input()
    compare_chars(value1, value2)
else:
    value1 = input()
    value2 = input()
    compare_string(value1, value2)
