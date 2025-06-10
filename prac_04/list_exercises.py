numbers = []
number1 = int(input("Number: "))
number2 = int(input("Number: "))
number3 = int(input("Number: "))
number4 = int(input("Number: "))
number5 = int(input("Number: "))
numbers.append(number1)
numbers.append(number2)
numbers.append(number3)
numbers.append(number4)
numbers.append(number5)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
def calculate_average(number):
    """calculate the average of numbers in the list"""
    return sum(number) / len(number)
average = calculate_average(numbers)
print(f"The average of the numbers is {average}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']