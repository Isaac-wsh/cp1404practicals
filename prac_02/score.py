"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

def main():
    score = int(input("Enter score: "))
    result = get_result(score)
    print(result)

    random_score = random.randint(0, 100)
    random_result = get_result(random_score)
    print(random_score)
    print(random_result)

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

# if 0 <= score <= 100:
#     if score >= 90:
#         print("Excellent")
#     elif score >= 50:
#         print("Passable")
#     else:
#         print("Bad")
# else:
#     print("Invalid score")
