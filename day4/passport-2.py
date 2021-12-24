import re


def check_creds(creds: dict) -> int:
    # print(creds.keys())
    if all(
        key in creds.keys() for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    ):
        # x byr (Birth Year) - four digits; at least 1920 and at most 2002.
        # x iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        # x eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        # x hgt (Height) - a number followed by either cm or in:
        # x If cm, the number must be at least 150 and at most 193.
        # x If in, the number must be at least 59 and at most 76.
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        # x ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        # x pid (Passport ID) - a nine-digit number, including leading zeroes.
        height, height_uom = creds["hgt"][:-2], creds["hgt"][-2:]
        print(f"h: {height}, uom: {height_uom}")
        if height_uom == "cm":
            valid_height = True if 193 >= int(height) >= 150 else False
        elif height_uom == "in":
            valid_height = True if 76 >= int(height) >= 59 else False
        else:
            valid_height = False

        # need hair color check - prob import re

        valid_hair_color = True if re.search("#[0-9,a-f]{6}", creds["hcl"]) else False
        print(valid_hair_color)

        if (
            2002 >= int(creds["byr"]) >= 1920
            and 2020 >= int(creds["iyr"]) >= 2010
            and 2030 >= int(creds["eyr"]) >= 2020
            and creds["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            and len(creds["pid"]) == 9
            and valid_height
            and valid_hair_color
        ):
            return 1
        else:
            return 0
    else:
        return 0


def main():
    with open("input.txt") as file:
        raw_input = file.read().splitlines()
    # print(raw_input)

    creds = {}
    valid_creds = 0
    for line in raw_input:
        if len(line) == 0:
            # passport = Passport(creds)
            # print(creds)
            valid_creds += check_creds(creds)
            creds = {}
        else:
            line_details = line.split()
            for detail in line_details:
                key, value = detail.split(":")
                creds[key] = value

    print(valid_creds)

    # print(creds)


if __name__ == "__main__":
    main()
