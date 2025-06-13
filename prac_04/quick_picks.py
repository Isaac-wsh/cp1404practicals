import random

PICK_NUMBER = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    pick_count = int(input("How many quick picks? "))
    count = 0
    while count < pick_count:
        pick = quick_pick()
        print(" ".join(f"{num:2}" for num in pick))
        """format numbers"""
        count = count + 1


def quick_pick():
    """Random pick 6 numbers"""
    numbers = []
    while len(numbers) < PICK_NUMBER:
        picked_number = random.randint(MIN_NUMBER,MAX_NUMBER)
        if picked_number not in numbers:
            numbers.append(picked_number)
    numbers.sort()
    return numbers

main()