import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("Number of quick picks: "))
    while number_of_quick_picks < 0:
        print("Invalid number of quick picks")
        number_of_quick_picks = int(input("Number of quick picks: "))
    for pick in range(number_of_quick_picks):
        quick_pick = []
        for n in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        # What would be another way to do this
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
