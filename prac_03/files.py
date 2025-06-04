#Ask the user for their name and write in file
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

#Print file contents
in_file = open("name.txt", "r")
name_in_file = in_file.read()
in_file.close()
print(f"Hi {name_in_file}!")

#Add numbers
with open("numbers.txt", "r") as file1:
    lines = file1.readlines()
    result = int(lines[0]) + int(lines[1])
    print(result)

#prints the total for all lines
with open("numbers.txt", "r") as file2:
    total = 0
    for line in file2:
        total = total + int(line)
    print(total)

