

if __name__ == "__main__":
    with open("input.txt") as f:
        input_list = f.readlines()

    number_list = [int(element.strip()) for element in input_list]

    for index, numb1 in enumerate(number_list):
        for index2, numb2 in enumerate(number_list):
            for index3, numb3 in enumerate(number_list):
                if numb1 + numb2 + numb3 == 2020:
                    print(numb1 * numb2 * numb3)