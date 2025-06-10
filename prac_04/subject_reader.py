"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)
    display_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    nested_list = []  # Create an empty list
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        nested_list.append(parts)  # Save the list to the created list
    input_file.close()
    return nested_list

def display_details(data):
    for detail in data:
        subject = detail[0]
        lecturer = detail[1]
        student_numbers = detail[2]
        print(f"{subject} is taught by {lecturer} and has {student_numbers} students")


main()