password = input("Enter your password: ")
length_pass = len(password)
while length_pass < 6:
    print("Your password is short. Please try another one.")
    password = input("Enter your password: ")
    length_pass = len(password)
print("*" * length_pass)