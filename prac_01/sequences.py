print("1. Show the even numbers from x to y")
print("2. Show the odd numbers from x to y")
print("3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)")
print("4. Exit the program")
print("Enter the number for using the function")
choice = input(">>> ")
while choice != "4":
    if choice == "1":
        x1 = int(input("Enter the number x: "))
        y1 = int(input("Enter the number y: "))
        for even in range(x1 , y1 + 1):
            if even % 2 == 0:
                print(even, end=" ")
        print()
    elif choice == "2":
        x2 = int(input("Enter the number x: "))
        y2 = int(input("Enter the number y: "))
        for odd in range(x2 , y2 + 1):
            if odd % 2 == 1:
                print(odd, end=" ")
        print()
    elif choice == "3":
        x3 = int(input("Enter the number x: "))
        y3 = int(input("Enter the number y: "))
        for square in range(x3, y3 + 1):
            print(square ** 2, end=" ")
        print()
    else:
        print("Invalid choice")
    print("1. Show the even numbers from x to y")
    print("2. Show the odd numbers from x to y")
    print("3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)")
    print("4. Exit the program")
    print("Enter the number for using the function")
    choice = input(">>> ")
print("Finished.")
