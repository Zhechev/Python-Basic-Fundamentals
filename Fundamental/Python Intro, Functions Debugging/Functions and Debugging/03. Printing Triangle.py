def print_top_pyramide(n):
    for i in range(1, n+1):
        for k in range(1, i+1):
            print(f'{k} ', end="")
        print()

def print_bottom_pyramide(n):
    for i in range(n, 1, -1):
        for k in range(1, i):
            print(f'{k} ', end="")
        print()


n = int(input())
print_top_pyramide(n)
print_bottom_pyramide(n)