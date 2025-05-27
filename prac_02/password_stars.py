def main():
    length_pass = get_password()
    print_stars(length_pass)


def print_stars(length_pass):
    print("*" * length_pass)


def get_password():
    password = input("Enter your password: ")
    length_pass = len(password)
    while length_pass < 6:
        print("Your password is short. Please try another one.")
        password = input("Enter your password: ")
        length_pass = len(password)
    return length_pass


main()