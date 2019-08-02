with open("input1.txt", "r") as f:
    lines = f.readlines()
    odd_line = []

    for i in range(0, len(lines)):
        if i % 2 != 0:
            odd_line.append(lines[i])

    with open('output.txt', "w") as f2:
        f2.writelines(odd_line)
