COLOR_TO_CODE = {"Absolute Zero": "#0048ba",
                 "Acid Green": "#b0bf1a",
                 "AliceBlue": "#f0f8ff",
                 "Alizarin crimson": "#e32636",
                 "Amaranth": "#e52b50",
                 "Amber": "#ffbf00",
                 "Amethyst": "#9966cc",
                 "AntiqueWhite": "#faebd7",
                 "Aqua": "#00ffff",
                 "Arylide Yellow": "#e9d66b"}
print(COLOR_TO_CODE)

input_name = input("Enter color name: ")
while input_name != "":
    name_separated = input_name.split(",")
    for code in name_separated:
        try:
            for dict_key in COLOR_TO_CODE:
                if user_input.casefold() == dict_key.casefold():
            print(f"{code:<17} is {COLOR_TO_CODE[code]}")
        except KeyError:
            print(f"{code:<17} is Invalid short state")
        color_code = input("Enter short state: ")