def main():
    password_length = 5
    valid_password = False
    password = get_password()
    while valid_password is False:
        if len(password) >= password_length:
            valid_password = True
        else:
            print("Invalid password")
            password = get_password()
    print_asterisk(password)


def print_asterisk(password):
    print('*' * len(password))


def get_password():
    password = input("Password: ")
    return password


main()
