type_of_projection = input()
rows = int(input())
cols = int(input())
rows_cols = rows * cols

if type_of_projection == 'Premiere':
    result = rows_cols * 12.00
elif type_of_projection == 'Normal':
    result = rows_cols * 7.50
else:
    result = rows_cols * 5.00

print(f'{result:.2f} leva')
