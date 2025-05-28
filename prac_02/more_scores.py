import random

def main():
    score = int(input("Enter score: "))
    result = get_result(score)

    random_score1 = random.randint(0, 100)
    random_result1 = get_result(random_score1)

    random_score2 = random.randint(0, 100)
    random_result2 = get_result(random_score2)

    random_score3 = random.randint(0, 100)
    random_result3 = get_result(random_score3)

    with open("results.txt", "w") as file:
        file.write(str(score) + " is " + result + "\n")
        file.write(str(random_score1) + " is " + random_result1 + "\n")
        file.write(str(random_score2) + " is " + random_result2 + "\n")
        file.write(str(random_score3) + " is " + random_result3 + "\n")

def get_result(score):
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