

def main():
    with open("input.txt") as file:
        raw_input = file.read().splitlines(keepends=False)

    unique_chars = set()
    total_unique_chars = 0
    init_set = True

    for row in raw_input:
        if len(row) == 0:
            # print(f"row: {row}, uc: {len(unique_chars)}")
            total_unique_chars += len(unique_chars)
            init_set = True
        else:
            if init_set:
                unique_chars = set(row)
                init_set = False
            else:
                intersect_row = set(row)
                unique_chars = set.intersection(unique_chars, intersect_row)

    print(total_unique_chars)


if __name__ == "__main__":
    main()


# 3366 - too high