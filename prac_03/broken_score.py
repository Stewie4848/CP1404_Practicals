def main():
    score = get_score()
    print(determine_grade(score))


def get_score():
    score = int(input("Score: "))
    return score


def determine_grade(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
