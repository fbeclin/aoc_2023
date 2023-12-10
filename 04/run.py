import regex as re


def getResultNumbers(line: str):
    card_part = line.split(" | ")
    card_left_part = card_part[0].split(":")
    card_winning_numbers = set(re.findall("\d+", card_left_part[1]))
    card_to_check_numbers = set(re.findall("\d+", card_part[1]))
    return card_winning_numbers.intersection(card_to_check_numbers)


def countWiningNumber(line: str):
    result = getResultNumbers(line)
    if len(result) != 0:
        return pow(2, len(result) - 1)
    return 0


def addCard(card_number: int, number: int, total_cards: dict):
    nb_cards = total_cards.get(card_number)
    if nb_cards is None:
        total_cards[card_number] = number
    else:
        total_cards[card_number] += number


def getCopiesOfWiningCards(line: str, card_number: int, total_cards: dict):
    addCard(card_number, 1, total_cards)
    [
        addCard(card_number + 1 + i, total_cards[card_number], total_cards)
        for i in range(len(getResultNumbers(line)))
    ]


def run1(filename: str):
    with open(filename) as file:
        print(sum([countWiningNumber(line.rstrip()) for line in file]))


def run2(filename: str):
    total_cards = dict()
    with open(filename) as file:
        [
            getCopiesOfWiningCards(line.rstrip(), index + 1, total_cards)
            for index, line in enumerate(file)
        ]
        print(sum(total_cards.values()))


if __name__ == "__main__":
    # filename = "sample.txt"
    filename = "input.txt"
    # run1(filename)
    run2(filename)
