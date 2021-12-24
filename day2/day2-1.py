

def main():
    with open("2-1_input.txt") as f:
        raw_input = f.readlines()

    pasword_list = [line.split() for line in raw_input]

    valid = 0
    for password in pasword_list:
        password_begin_range = int(password[0].split('-')[0])
        password_end_range = int(password[0].split('-')[-1])
        password_char = password[1][0]
        saved_password = password[2]
        # print(password, password_begin_range, password_end_range, password_char, saved_password)
        chars_in_saved_password = 0
        for char in saved_password:
            if char == password_char:
                chars_in_saved_password += 1
        # print(chars_in_saved_password)

        if password_begin_range <= chars_in_saved_password <= password_end_range:
            valid += 1
    print(valid)




if __name__ == "__main__":
    main()
