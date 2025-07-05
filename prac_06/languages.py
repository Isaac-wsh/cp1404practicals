from programming_language import ProgrammingLanguage

def main():
    """Run the program"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for l in languages:
        if l.is_dynamic():
            print(l.language)


main()