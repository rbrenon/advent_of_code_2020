from collections import Counter


def main():
    with open("input.txt") as file:
        raw_data = file.read().splitlines()
        data = [int(element) for element in raw_data]
        data = sorted(data)
        data = [0] + data + [data[-1] + 3]
    part_one(data)
    part_two(data)


def part_one(data: list) -> None:
    # ones = 0
    # threes = 0
    # if data[0] - 1 == 0:
    #     ones += 1
    # else:
    #     threes += 1
    # for i, num in enumerate(data):
    #     try:
    #         if data[i+1] - num == 1:
    #             ones += 1
    #         elif data[i+1] - num == 3:
    #             threes += 1
    #     except IndexError:
    #         threes += 1
    #
    # print(f"1's: {ones} * 3's: {threes} = {ones * threes}")     # 1998

    counter = Counter(data[i + 1] - val for i, val in enumerate(data[:-1]))

    print(f"1's: {counter[1]} * 3's: {counter[3]} = {counter[1] * counter[3]}")  # 1998


def part_two(data: list):
    data.pop(0)
    valid_combos = {0: 1}

    for adapter in data:
        valid_combos[adapter] = (
            valid_combos.get(adapter - 3, 0)
            + valid_combos.get(adapter - 2, 0)
            + valid_combos.get(adapter - 1, 0)
        )

    print(f"valid combos: {valid_combos[data[-1]]}")    # 347250213298688


if __name__ == "__main__":
    main()
