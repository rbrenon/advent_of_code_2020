# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)


class Passport:
    def __init__(self, creds):
        self.byr = None
        self.iry = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None
        self.valid = self.validation_check()

    def validation_check(self):
        if all(
            self.byr,
            self.iry,
            self.eyr,
            self.hgt,
            self.hcl,
            self.ecl,
            self.pid,
            self.cid,
        ):
            return True
        else:
            return False


def check_creds(creds: dict) -> int:
    print(creds.keys())
    if all(
        key in creds.keys() for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    ):  # "cid"
        return 1
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
            print(creds)
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
