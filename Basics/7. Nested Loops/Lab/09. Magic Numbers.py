n = int(input())
row = ''

for a in range(0, 9):
    for b in range(0, 9):
        for c in range(0, 9):
            for d in range(0, 9):
                for e in range(0, 9):
                    for f in range(0, 9):
                        if a * b * c * d * e * f == n:
                            row += f'{a}{b}{c}{d}{e}{f} '

print(row)
