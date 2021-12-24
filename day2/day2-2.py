

def main():
    with open("2-1_input.txt") as f:
        raw_input = f.readlines()

    pasword_list = [line.split() for line in raw_input]

    valid = 0
    for password in pasword_list:
        password_begin_position = int(password[0].split('-')[0])
        password_end_position = int(password[0].split('-')[-1])
        password_char = password[1][0]
        saved_password = password[2]
        # print(password, password_begin_position, password_end_position, password_char, saved_password)
        chars_in_saved_password = 0

        if saved_password[password_begin_position-1] == password_char:
            chars_in_saved_password += 1
        if saved_password[password_end_position-1] == password_char:
            chars_in_saved_password += 1

        if chars_in_saved_password == 1:
            valid += 1
    print(valid)


if __name__ == "__main__":
    main()
