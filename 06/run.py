import datetime
import regex as re


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

    print(f"times: {times}, distances: {distances}")


def run2(filename: str):
    pass


if __name__ == "__main__":
    # get the start datetime
    st = datetime.datetime.now()
    filename = "sample.txt"
    # filename = "input.txt"
    run1(filename)
    # run2(filename)

    # get the end datetime
    et = datetime.datetime.now()

    # get execution time
    elapsed_time = et - st
    print("Execution time:", elapsed_time, "seconds")
