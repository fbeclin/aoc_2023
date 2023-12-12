import datetime
from functools import reduce
from math import ceil, floor, sqrt
from operator import mul
import regex as re


def getNumberOfWayToWinTheRace(time: int, distance: int):
    # distance = time * speed
    # distance < (time - h) * h
    # we have a quadratic inequality
    # h² + h*time - distance > 0
    # discriminent is b² - 4ac which is time² - 4*distance
    # time² in input is always > 4*distance
    # which leads to 2 solutions
    # we need only the inner interval and only integer values
    a = floor((-time - sqrt(pow(time, 2) - 4 * distance)) / 2)
    b = ceil((-time + sqrt(pow(time, 2) - 4 * distance)) / 2)

    return b - a - 1


def run1(filename: str):
    with open(filename) as file:
        times = []
        distances = []
        for line in enumerate(file):
            if line[0] == 0:
                times = list(
                    map(
                        lambda x: int(x),
                        re.findall("\d+", line[1].rstrip().split(":")[1]),
                    )
                )
            if line[0] == 1:
                distances = list(
                    map(
                        lambda x: int(x),
                        re.findall("\d+", line[1].rstrip().split(":")[1]),
                    )
                )
        print(
            reduce(
                mul,
                [
                    getNumberOfWayToWinTheRace(time, distances[i])
                    for i, time in enumerate(times)
                ],
            )
        )


def run2(filename: str):
    with open(filename) as file:
        for line in enumerate(file):
            if line[0] == 0:
                time = int("".join(re.findall("\d+", line[1].rstrip().split(":")[1])))
            if line[0] == 1:
                distance = int(
                    "".join(re.findall("\d+", line[1].rstrip().split(":")[1]))
                )
        print(getNumberOfWayToWinTheRace(time, distance))


if __name__ == "__main__":
    # get the start datetime
    st = datetime.datetime.now()
    # filename = "sample.txt"
    filename = "input.txt"
    # run1(filename)
    run2(filename)

    # get the end datetime
    et = datetime.datetime.now()

    # get execution time
    elapsed_time = et - st
    print("Execution time:", elapsed_time, "seconds")
