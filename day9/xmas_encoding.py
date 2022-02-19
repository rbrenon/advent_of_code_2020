preamble = 25


def main():
    with open("input.txt") as file:
        raw_data = file.read().splitlines()
        data = [int(element) for element in raw_data]

    part_one(data)


def part_one(data: list) -> None:
    # print(type(data), data)
    for index, element in enumerate(data):
        if index < preamble:
            pass
        else:
            valid = False
            previous_preamble = data[index-preamble:index]
            # print(previous_5)
            for number in previous_preamble:
                if element-number in previous_preamble:
                    valid = True
            if not valid:
                invalid_number = element
                print(f"{index} number not valid: {invalid_number}")   # 1124361034

                part_two(data, invalid_number)


def part_two(data: list, number: int) -> None:
    # print(number)
    for first_index, first_num in enumerate(data):
        for second_index, second_num in enumerate(data[first_index+1:]):
            total = 0
            subset_to_sum = data[first_index:second_index+first_index]
            # print(subset_to_sum)
            total = sum(subset_to_sum)

            if total == number:
                subset_to_sum = sorted(subset_to_sum)
                print(f"winner: {subset_to_sum[0]} + {subset_to_sum[-1]} = {subset_to_sum[0] + subset_to_sum[-1]} - total = {total}, number = {number}")
            elif total > number:
            #     print(f"total: {total} - index 1: {first_index}, index 2: {second_index}, num 1: {first_num}, num 2: {second_num}")
                break

#   too low
#   48 272 979
#   122 981 070

#   too high
#   1 124 455 043
#   2 432 941 083

#   not correct
#   120 667 260

#   correct
#   129 444 555

if __name__ == "__main__":
    main()