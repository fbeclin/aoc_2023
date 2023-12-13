import datetime
from itertools import count


def fillWithPrediction(history: []):
    predictions = [history]
    # i'm stupid
    while predictions[-1].count(0) != len(predictions[-1]):
        next_prediction = predictions[-1]
        values = [
            next_prediction[i + 1] - next_prediction[i]
            for i in range(0, len(next_prediction) - 1)
        ]
        predictions.append(values)
    return predictions


def getExtrapolatedValues(history: []):
    predictions = fillWithPrediction(history)

    # add last 0 for last prediction
    predictions[-1].append(0)
    predictions = list(reversed(predictions))

    for i, prediction in enumerate(predictions[:-1]):
        predictions[i + 1].append(prediction[-1] + predictions[i + 1][-1])

    return predictions[-1][-1]


def getExtrapolatedValuesToLeft(history: []):
    predictions = fillWithPrediction(history)

    # add last 0 for last prediction
    predictions[-1].insert(0, 0)
    predictions = list(reversed(predictions))
    for i, prediction in enumerate(predictions[:-1]):
        predictions[i + 1].insert(0, -prediction[0] + predictions[i + 1][0])

    return predictions[-1][0]


def run1(filename: str):
    with open(filename) as file:
        print(
            sum(
                [
                    getExtrapolatedValues(
                        list(map(lambda x: int(x), line.rstrip().split(" ")))
                    )
                    for line in file
                ]
            )
        )


def run2(filename: str):
    with open(filename) as file:
        print(
            sum(
                [
                    getExtrapolatedValuesToLeft(
                        list(map(lambda x: int(x), line.rstrip().split(" ")))
                    )
                    for line in file
                ]
            )
        )


if __name__ == "__main__":
    # get the start datetime
    st = datetime.datetime.now()
    # filename = "sample.txt"
    # filename = "sample2.txt"
    filename = "input.txt"
    # run1(filename)
    run2(filename)

    # get the end datetime
    et = datetime.datetime.now()

    # get execution time
    elapsed_time = et - st
    print("Execution time:", elapsed_time, "seconds")
