with open("input1.txt", "r") as input1_file:

    lines_input1 = input1_file.readlines()

    with open("input2.txt", "r") as input2_file:
        lines_input2 = input2_file.readlines()
        result = []

        for line in range(0, len(lines_input1)):
            result.append(lines_input1[line])
            result.append(lines_input2[line])


with open("output.txt", "w") as output_file:
    output_file.writelines(result)
