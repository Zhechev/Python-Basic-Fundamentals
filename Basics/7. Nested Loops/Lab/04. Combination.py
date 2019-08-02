n = int(input())
counter = 0

for a in range(0, n+1):
    for b in range(0, n+1):
        for c in range(0, n+1):
            for d in range(0, n+1):
                for e in range(0, n+1):
                    if a + b + c + d + e == n:
                        counter += 1

print(counter)
