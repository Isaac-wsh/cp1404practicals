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

lower_color_dict = {}
for name in COLOR_TO_CODE:
    lower_color_dict[name.lower()] = name

input_name = input("Enter color name: ")
while input_name != "":
    name_separated = input_name.split(",")
    for color in name_separated:
        color = color.strip().lower()
        try :
            original_name = lower_color_dict[color]
            print(f"{original_name:<20} is {COLOR_TO_CODE[original_name]}")
        except KeyError:
            print(f"{color:<20} is Invalid color name")
    input_name = input("Enter color name: ")