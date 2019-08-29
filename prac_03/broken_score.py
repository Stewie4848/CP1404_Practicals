def main():
    score = get_score()
    print(determine_score(score))


def get_score():
    score = int(input("Score: "))
    return score


def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "Fail"


main()
