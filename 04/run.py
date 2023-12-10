import regex as re


def countWiningNumber(line: str):
    card_part = line.split(" | ")
    card_left_part = card_part[0].split(":")
    card_winning_numbers = set(re.findall("\d+", card_left_part[1]))
    card_to_check_numbers = set(re.findall("\d+", card_part[1]))

    result = card_winning_numbers.intersection(card_to_check_numbers)
    if len(result) != 0:
        return pow(2, len(result) - 1)
    return 0


def run1(filename: str):
    with open(filename) as file:
        print(sum([countWiningNumber(line.rstrip()) for line in file]))


def run2(filename: str):
    pass


if __name__ == "__main__":
    # filename = "sample.txt"
    filename = "input.txt"
    run1(filename)
    # run2(filename)
