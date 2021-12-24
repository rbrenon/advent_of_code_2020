
def main():
    with open("input.txt") as file:
        raw_input = file.read().splitlines()

    seat_codes = []
    for line in raw_input:
        seat = []
        for element in line:
            if element in ["B", "R"]:
                seat.append("1")
            else:
                seat.append("0")
        seat_codes.append(seat)

    # print(seat_codes)

    seat_id = []
    for seat_code in seat_codes:
        code = "".join([element for element in seat_code])
        # print(code)
        # print(int(code, 2))
        seat_id.append(int(code, 2))

    print(max(seat_id))
    # print(sorted(seat_id))

    not_found = []

    for seat_numb in range(835):
        if seat_numb not in seat_id:
            not_found.append(seat_numb)

    print(not_found)

if __name__ == "__main__":
    main()