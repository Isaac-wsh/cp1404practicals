MENU = """
(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit
"""

def main():
    valid_score = None
    print(MENU)
    choice = input("Make a choice: ")
    while choice != "Q":
        if choice == "G":
            valid_score = get_score()
        elif choice == "P":
            if valid_score is None:
                print("Choose G first")
            else:
                # valid_score = get_score()
                print(get_result(valid_score))
        elif choice == "S":
            if valid_score is None:
                print("Choose G first")
            else:
                # valid_score = get_score()
                print("*" * valid_score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Make a choice: ")
    print("farewell")


def get_score():
    """Get the score"""
    score = int(input("Enter a score: "))
    while score < 0 or score > 100:
        print("Invalid score.")
        score = int(input("Enter a score: "))
    return score

def get_result(score):
    """Determine the level of results"""
    if 0 > score or score> 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"
main()