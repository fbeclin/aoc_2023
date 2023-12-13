import datetime
import functools
import regex as re


start_node = "AAA"
end_node = "ZZZ"


def fillNodes(line: str, nodes: dict):
    node = re.findall("[A-Z]{3}", line)
    nodes[node[0]] = (node[1], node[2])


def runThrough(direction: str, nodes: dict):
    # no graph algorithm, pure brainless
    nb_step = 0
    dir_index = 0
    current_node = start_node
    while current_node != end_node:
        current_node_children = nodes[current_node]
        current_direction = direction[dir_index]
        current_node = (
            current_node_children[0]
            if current_direction == "L"
            else current_node_children[1]
        )
        dir_index = (dir_index + 1) % len(direction)
        nb_step += 1
    return nb_step


def run1(filename: str):
    direction = ""
    nodes = dict()
    with open(filename) as file:
        direction = file.readline().rstrip()
        file.readline().rstrip()
        [fillNodes(line.rstrip(), nodes) for line in file]

    print(runThrough(direction, nodes))


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
