width_of_free_space = int(input())
length_of_free_space = int(input())
height_of_free_space = int(input())

km = width_of_free_space * length_of_free_space * height_of_free_space
km_kartons = 0

n = input()

while n != 'Done':
    km_kartons += int(n)
    if km < km_kartons:
        result = km_kartons - km
        print(f'No more free space! You need {result} Cubic meters more.')
        exit()
    n = input()

result = km - km_kartons
print(f'{result} Cubic meters left.')
