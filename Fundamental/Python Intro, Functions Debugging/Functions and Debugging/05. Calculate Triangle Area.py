def calc_triangle_area(n, h):
    if isinstance(n, int) or isinstance(h, int):
        area = (int(n) * int(h)) // 2
        print(f'{area}')
    else:
        area = (n * h) / 2
        print(f'{format(area)}')


n = float(input())
h = float(input())
calc_triangle_area(n, h)
