"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "":
    code_upper = state_code.upper()
    if code_upper in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[code_upper])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
