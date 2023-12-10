from functools import reduce
from typing import Tuple


def hasGearAdjacentToLetter(lineIndex: int, letterIndex: int, lines: [str]) -> bool:
    if (
        lineIndex < 0
        or lineIndex == len(lines[0])
        or letterIndex < 0
        or letterIndex == len(lines[0])
    ):
        return False
    return lines[lineIndex][letterIndex] == "*"


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


def getGearAdjacentPos(
    lineIndex: int, letterIndex: int, lines: [str]
) -> Tuple[int, int]:
    # above
    if hasGearAdjacentToLetter(lineIndex - 1, letterIndex - 1, lines):
        return (lineIndex - 1, letterIndex - 1)
    if hasGearAdjacentToLetter(lineIndex - 1, letterIndex, lines):
        return (lineIndex - 1, letterIndex)
    if hasGearAdjacentToLetter(lineIndex - 1, letterIndex + 1, lines):
        return (lineIndex - 1, letterIndex + 1)

    # same line
    if hasGearAdjacentToLetter(lineIndex, letterIndex - 1, lines):
        return (lineIndex, letterIndex - 1)
    if hasGearAdjacentToLetter(lineIndex, letterIndex + 1, lines):
        return (lineIndex, letterIndex + 1)

    # below
    if hasGearAdjacentToLetter(lineIndex + 1, letterIndex - 1, lines):
        return (lineIndex + 1, letterIndex - 1)
    if hasGearAdjacentToLetter(lineIndex + 1, letterIndex, lines):
        return (lineIndex + 1, letterIndex)
    if hasGearAdjacentToLetter(lineIndex + 1, letterIndex + 1, lines):
        return (lineIndex + 1, letterIndex + 1)
    return None


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


def addNumberPartToGearPos(part_number: str, adjGearPos: Tuple[int, int], gears: dict):
    # print(f"addNumberPartToGearPos, adjGearPos: {adjGearPos} ; part_number:{part_number}")
    gearPos = gears.get(adjGearPos)
    if gearPos is None:
        gears[adjGearPos] = [int(part_number)]
    else:
        gears[adjGearPos].append(int(part_number))
    # input()


def run2(filename: str):
    with open(filename) as file:
        # read all lines
        lines = file.read().splitlines()

        gears = dict()

        for i in range(len(lines)):
            part_number = ""
            adjGearPos = None
            for j in range(len(lines[0])):
                if lines[i][j].isdigit():
                    part_number += lines[i][j]
                    # check if any gear adjacent
                    if adjGearPos is None:
                        adjGearPos = getGearAdjacentPos(i, j, lines)
                else:
                    if adjGearPos is not None:
                        # add number to this gear position
                        addNumberPartToGearPos(part_number, adjGearPos, gears)
                    part_number = ""
                    adjGearPos = None
            if adjGearPos is not None:
                # add number to this gear position
                addNumberPartToGearPos(part_number, adjGearPos, gears)

        print(
            sum(
                [
                    reduce((lambda x, y: x * y), gear)
                    for gear in gears.values()
                    if len(gear) == 2
                ]
            )
        )


if __name__ == "__main__":
    # filename = "sample.txt"
    filename = "input.txt"
    # run1(filename)
    run2(filename)
