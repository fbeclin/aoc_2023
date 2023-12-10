from operator import concat
import regex as re


def hasSymAdjacentToLetter(lineIndex: int, letterIndex: int, lines: [str]) -> bool:
    if (
        lineIndex < 0
        or lineIndex == len(lines[0])
        or letterIndex < 0
        or letterIndex == len(lines[0])
    ):
        return False
    return (
        not lines[lineIndex][letterIndex].isalnum()
        and lines[lineIndex][letterIndex] != "."
    )


def hasSymbAdjacent(lineIndex: int, letterIndex: int, lines: [str]) -> bool:
    # above
    if (
        hasSymAdjacentToLetter(lineIndex - 1, letterIndex - 1, lines)
        or hasSymAdjacentToLetter(lineIndex - 1, letterIndex, lines)
        or hasSymAdjacentToLetter(lineIndex - 1, letterIndex + 1, lines)
    ):
        return True
    # same line
    if hasSymAdjacentToLetter(
        lineIndex, letterIndex - 1, lines
    ) or hasSymAdjacentToLetter(lineIndex, letterIndex + 1, lines):
        return True
    # below
    if (
        hasSymAdjacentToLetter(lineIndex + 1, letterIndex - 1, lines)
        or hasSymAdjacentToLetter(lineIndex + 1, letterIndex, lines)
        or hasSymAdjacentToLetter(lineIndex + 1, letterIndex + 1, lines)
    ):
        return True
    return False


def run1(filename: str):
    with open(filename) as file:
        # read all lines
        lines = file.read().splitlines()

        numbers = []

        for i in range(len(lines)):
            part_number = ""
            isAdjacent = False
            for j in range(len(lines[0])):
                if lines[i][j].isdigit():
                    part_number += lines[i][j]
                    # check if any symbol adjacent
                    if not isAdjacent and hasSymbAdjacent(i, j, lines):
                        isAdjacent = True
                else:
                    if isAdjacent:
                        numbers.append(int(part_number))
                    part_number = ""
                    isAdjacent = False
            if isAdjacent:
                numbers.append(int(part_number))

        print(sum(numbers))


def run2(filename: str):
    pass
    # with open(filename) as file:
    #     print(sum([powerOfminCubes(line.rstrip()) for line in file]))


if __name__ == "__main__":
    # filename = "sample.txt"
    filename = "input.txt"
    run1(filename)
    # run2(filename)
