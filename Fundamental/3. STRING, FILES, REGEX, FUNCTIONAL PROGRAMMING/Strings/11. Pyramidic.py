n = int(input())
i = 1
all_lines = {}

while n > 0:

    input_line = input()

    all_lines[i] = input_line

    i += 1
    n -= 1

for key, line in all_lines.items():
    for char in line:
        if key+1 in all_lines:
            if all_lines[key+1].count(char) == (int(key) * 2 + 1):
                all_lines[key] = char*((int(key) * 2) - 1)

for key, line in all_lines.items():
    print(f"{line}")

