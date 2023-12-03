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


def run1(filename: str):
    with open(filename) as file:
        print(sum([getNumberFromFirstAndLastDigit(line.rstrip()) for line in file]))


if __name__ == "__main__":
    # filename = "sample.txt"
    filename = "input01.txt"
    run1(filename)
