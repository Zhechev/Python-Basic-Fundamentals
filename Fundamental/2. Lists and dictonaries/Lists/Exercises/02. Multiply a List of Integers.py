def multiply(num, multiplier):
    return num * multiplier


list_numbers = list(map(int, input().split(' ')))
multyplier = int(input())
multiplied_list = list(map(str, [multiply(el, multyplier) for el in list_numbers]))

print(' '.join(multiplied_list))
