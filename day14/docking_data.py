

def main():
    with open("input.txt") as file:
        raw_input = file.read().splitlines()

    print(f"Part one: {part_one(raw_input)}")   # 6513443633260


def part_one(docking_instructions: list[str]) -> int:
    memory_bank = dict()

    for line in docking_instructions:  # mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
        if "mask" in line.split():
            bit_mask: str = line.split()[
                -1
            ]  # bit_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        else:  # line = 'mem[8] = 0'
            memory_instruction: list[str] = (
                line.replace("mem", "").replace("[", "").replace("]", "").split(" = ")
            )  # ['8', '0']
            memory_location: int = int(memory_instruction[0])  # 8
            instruction_value: int = int(memory_instruction[-1])  # 0

            masked_instruction_value_to_store = calc_value_to_store(bit_mask, instruction_value)

            memory_bank[memory_location] = masked_instruction_value_to_store

    return sum(memory_bank.values())


def calc_value_to_store(bit_mask: str, instruction_value: int) -> int:
    """
    applies bit mask to instruction value to calculate the value to be saved in memory
    :param bit_mask:
    :param instruction_value:
    :return:
    """

    # find the location (index) and value of the mask bits
    mask_locations_and_values: list[tuple[int, str]] = [
        (index, value) for index, value in enumerate(bit_mask) if value != "X"
    ]   # [(29, 1), (34, 0)]

    # convert instruction value to binary
    instruction_value_as_binary: str = f"{instruction_value:036b}"   # '000000000000000000000000000000001011'

    masked_value = instruction_value_as_binary[:]
    # mask values
    for location, value in mask_locations_and_values:
        masked_value = masked_value[:location] + value + masked_value[location+1:]

    # convert back to integer
    value_to_store = int(masked_value, 2)
    return value_to_store


if __name__ == "__main__":
    main()
