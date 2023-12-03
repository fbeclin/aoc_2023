from operator import concat
import regex as re

pattern = "Game (\d+)"
pattern_cube = " (\d+) (blue|red|green)(,|;)?"

max_cubes = {"red": 12, "green": 13, "blue": 14}


def countCubes(line: str) -> int:
    input_split = line.split(":")
    game_id = re.match(pattern, input_split[0])[1]

    for cs in re.findall(pattern_cube, input_split[1]):
        if int(cs[0]) > max_cubes[cs[1]]:
            return 0
    return int(game_id)


def run1(filename: str):
    with open(filename) as file:
        print(sum([countCubes(line.rstrip()) for line in file]))


def run2(filename: str):
    pass


if __name__ == "__main__":
    # filename = "sample.txt"
    filename = "input.txt"
    run1(filename)
    # run2(filename)
