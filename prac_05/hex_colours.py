CODE_TO_COLOR = {"Absolute Zero": "#0048ba",
                 "Acid Green": "#b0bf1a",
                 "AliceBlue": "#f0f8ff",
                 "Alizarin crimson": "#e32636",
                 "Amaranth": "#e52b50",
                 "Amber": "#ffbf00",
                 "Amethyst": "#9966cc",
                 "AntiqueWhite": "#faebd7",
                 "Aqua": "#00ffff",
                 "Arylide Yellow": "#e9d66b"}
print(CODE_TO_COLOR)

state_code = input("Enter short state: ")
while state_code != "":
    code_upper = state_code.upper().split()
    for code in code_upper:
        try:
            print(f"{code:<4} is {CODE_TO_NAME[code]}")
        except KeyError:
            print(f"{code:<4} is Invalid short state")
    state_code = input("Enter short state: ")