import re


def main():
    with open("testinput.txt") as file:
        raw_input = file.read().splitlines()

    # part_1(raw_input)
    part_2(raw_input)


def part_1(input):
    command_codes = []
    for line in input:
        operation = line.split()[0]
        argument = int(line.split()[1])
        command_codes.append([operation, argument])

    index, accumulator = 0, 0
    processed = []
    while index not in processed:
        command = command_codes[index]
        match command[0]:
            case "nop":
                processed.append(index)
                index += 1
            case "acc":
                processed.append(index)
                accumulator += command[1]
                index += 1
            case "jmp":
                processed.append(index)
                index += command[1]
    print(f"Part 1: {accumulator}")  # 1262


def part_2(input):
    command_codes = []
    for line in input:
        operation = line.split()[0]
        argument = int(line.split()[1])
        command_codes.append([operation, argument])
    print(command_codes)

    # create list of nops and jmps
    code_index_to_check = []
    for index, code in enumerate(command_codes):
        if "nop" in code or "jmp" in code:
            code_index_to_check.append(index)

    # cycle through changing 1 at a time until the full program executes


    for code_index in code_index_to_check:
        index, accumulator = 0, 0
        processed = []
        while index not in processed:
            if index in code_index:
                if command_codes[index] == "jmp":
                    
            else:
                command = command_codes[index]
            match command[0]:
                case "nop":
                    processed.append(index)
                    index += 1
                case "acc":
                    processed.append(index)
                    accumulator += command[1]
                    index += 1
                case "jmp":
                    processed.append(index)
                    index += command[1]

    print(code_index_to_check)



if __name__ == "__main__":
    main()