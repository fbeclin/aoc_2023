import datetime
import functools
import regex as re

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

card_value = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def readHand(handWithBid: []):
    count_dict = {}
    for card in handWithBid[0]:
        count = count_dict.get(card)
        if count is None:
            count = 0
        count_dict[card] = count + 1

    nb_same_keys = count_dict.keys()
    if len(nb_same_keys) == 1:
        five_of_a_kind.append(handWithBid)
    elif len(nb_same_keys) == 2:
        # either four or kind or full house
        if list(count_dict.values())[0] == 1 or list(count_dict.values())[0] == 4:
            four_of_a_kind.append(handWithBid)
        else:
            full_house.append(handWithBid)
    elif len(nb_same_keys) == 3:
        # either three of a kind or two pairs
        if max(count_dict.values()) == 3:
            three_of_a_kind.append(handWithBid)
        else:
            two_pair.append(handWithBid)
    elif len(nb_same_keys) == 4:
        one_pair.append(handWithBid)
    else:
        high_card.append(handWithBid)


def compare(hand_x, hand_y):
    for i, card in enumerate(hand_x[0]):
        compare_to = card_value[card] - card_value[hand_y[0][i]]
        if compare_to != 0:
            return compare_to
    return 0


def sortArrays():
    five_of_a_kind.sort(key=functools.cmp_to_key(compare))
    four_of_a_kind.sort(key=functools.cmp_to_key(compare))
    full_house.sort(key=functools.cmp_to_key(compare))
    three_of_a_kind.sort(key=functools.cmp_to_key(compare))
    two_pair.sort(key=functools.cmp_to_key(compare))
    one_pair.sort(key=functools.cmp_to_key(compare))
    high_card.sort(key=functools.cmp_to_key(compare))


def computeWiningInArray(card_array: [], startIndex: int):
    # [
    #     print(f"{i + 1 + startIndex} * {int(hand[1])}")
    #     for i, hand in enumerate(card_array)
    # ]
    return sum(
        [(i + 1 + startIndex) * int(hand[1]) for i, hand in enumerate(card_array)]
    )


def computeWining():
    rank = 0
    high_card_wining = computeWiningInArray(high_card, rank)
    rank += len(high_card)
    one_pair_wining = computeWiningInArray(one_pair, rank)
    rank += len(one_pair)
    two_pair_wining = computeWiningInArray(two_pair, rank)
    rank += len(two_pair)
    three_of_a_kind_wining = computeWiningInArray(three_of_a_kind, rank)
    rank += len(three_of_a_kind)
    full_house_wining = computeWiningInArray(full_house, rank)
    rank += len(full_house)
    four_of_a_kind_wining = computeWiningInArray(four_of_a_kind, rank)
    rank += len(four_of_a_kind)
    five_of_a_kind_wining = computeWiningInArray(five_of_a_kind, rank)
    print(
        high_card_wining
        + one_pair_wining
        + two_pair_wining
        + three_of_a_kind_wining
        + full_house_wining
        + four_of_a_kind_wining
        + five_of_a_kind_wining
    )


def debug():
    print(f"five_of_a_kind: {five_of_a_kind}")
    print(f"four_of_a_kind: {four_of_a_kind}")
    print(f"full_house: {full_house}")
    print(f"three_of_a_kind: {three_of_a_kind}")
    print(f"two_pair: {two_pair}")
    print(f"one_pair: {one_pair}")
    print(f"high_card: {high_card}")


def run1(filename: str):
    with open(filename) as file:
        [readHand(line.rstrip().split(" ")) for line in file]
    # debug()

    # sort arrays
    sortArrays()
    # debug()

    # compute wining
    computeWining()


def run2(filename: str):
    pass


if __name__ == "__main__":
    # get the start datetime
    st = datetime.datetime.now()
    # filename = "sample.txt"
    filename = "input.txt"
    run1(filename)
    # run2(filename)

    # get the end datetime
    et = datetime.datetime.now()

    # get execution time
    elapsed_time = et - st
    print("Execution time:", elapsed_time, "seconds")
