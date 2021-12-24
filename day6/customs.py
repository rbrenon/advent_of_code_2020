

def main():
    with open("input.txt") as file:
        raw_input = file.read().splitlines(keepends=False)

    # print(raw_input)

    # for row in raw_input:
    #     print(f"{row} len={len(row)}")

    unique_chars = set()
    total_unique_chars = 0

    for row in raw_input:
        if len(row) == 0:
            # print(f"row: {row}, uc: {len(unique_chars)}")
            total_unique_chars += len(unique_chars)
            unique_chars = set()
        else:
            unique_chars = set.union(unique_chars, row)

    print(total_unique_chars)


if __name__ == "__main__":
    main()