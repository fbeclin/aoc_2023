from operator import concat
import regex as re


digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
pattern = str.join("|", concat(list(digits.keys()), list(digits.values())))


def getNumberFromFirstAndLastDigit(line: str) -> int:
    first_digit = ""
    last_digit = ""
    for letter in line:
        if str.isdigit(letter):
            first_digit = letter
            break
    for letter in reversed(line):
        if str.isdigit(letter):
            last_digit = letter
            break
    return int(first_digit + last_digit)


def getNumberWithRegex(line: str) -> int:
    matches = re.findall(pattern, line, overlapped=True)
    number = int(
        digits.get(matches[0], matches[0]) + digits.get(matches[-1], matches[-1])
    )
    return number


def run1(filename: str):
    with open(filename) as file:
        print(sum([getNumberFromFirstAndLastDigit(line.rstrip()) for line in file]))


def run2(filename: str):
    with open(filename) as file:
        print(sum([getNumberWithRegex(line.rstrip()) for line in file]))


if __name__ == "__main__":
    # filename = "sample2.txt"
    filename = "input.txt"
    # run1(filename)
    run2(filename)
