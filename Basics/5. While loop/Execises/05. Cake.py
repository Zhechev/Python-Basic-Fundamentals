width = int(input())
height = int(input())

size = width * height
all_pieces = 0

while size >= 0:
    pieces = input()
    if pieces == 'STOP':
        print(f'{size} pieces are left.')
        exit()
    size -= int(pieces)
    all_pieces += int(pieces)

print(f'No more cake left! You need {all_pieces - (width * height)} pieces more.')
