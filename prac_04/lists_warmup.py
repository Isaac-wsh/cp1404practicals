numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] output: 3
# numbers[-1] output: 2
# numbers[3] output: 1
# numbers[:-1] output: [3, 1, 4, 1, 5, 9]
# numbers[3:4] output: [1]
# 5 in numbers output: True
# 7 in numbers output: False
# "3" in numbers output: False
# numbers + [6, 5, 3] output: [3, 1, 4, 1, 5, 9, 6, 5, 3]

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
print(9 in numbers)