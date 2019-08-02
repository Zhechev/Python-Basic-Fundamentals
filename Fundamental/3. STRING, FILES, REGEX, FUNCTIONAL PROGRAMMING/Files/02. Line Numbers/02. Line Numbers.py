with open("input1.txt", "r") as input_file:
    lines = input_file.readlines()
    lines_list = []

    for line in range(0, len(lines)):
        row = str(line+1) + '. ' + str(lines[line])
        lines_list.append(row)

with open("output.txt", "w") as output_file:
    output_file.writelines(lines_list)
