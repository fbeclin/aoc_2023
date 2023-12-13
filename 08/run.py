import datetime
import functools
from math import lcm
import regex as re


start_node = "AAA"
end_node = "ZZZ"


def fillNodes(line: str, nodes: dict):
    node = re.findall("[A-Z0-9]{3}", line)
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


def runThroughSimultaneously(direction: str, nodes: dict):
    # no graph algorithm, pure brainless
    nb_step = 0
    dir_index = 0
    already_visited_nodes_length = []
    start_nodes = [node for node in list(nodes.keys()) if node[2] == "A"]

    current_nodes = start_nodes
    while len(current_nodes) > 0:
        next_nodes = []
        for node in current_nodes:
            current_node_children = nodes[node]
            current_direction = direction[dir_index]
            next_node = (
                current_node_children[0]
                if current_direction == "L"
                else current_node_children[1]
            )
            # if not already at end
            # span should reduce once each node reaches end
            if next_node[2] != "Z":
                next_nodes.append(next_node)
            else:
                already_visited_nodes_length.append(nb_step + 1)

        # replace current nodes by next nodes
        current_nodes = next_nodes
        dir_index = (dir_index + 1) % len(direction)
        nb_step += 1

    return lcm(*already_visited_nodes_length)


def run1(filename: str):
    direction = ""
    nodes = dict()
    with open(filename) as file:
        direction = file.readline().rstrip()
        file.readline().rstrip()
        [fillNodes(line.rstrip(), nodes) for line in file]

    print(runThrough(direction, nodes))


def run2(filename: str):
    direction = ""
    nodes = dict()
    with open(filename) as file:
        direction = file.readline().rstrip()
        file.readline().rstrip()
        [fillNodes(line.rstrip(), nodes) for line in file]

    print(runThroughSimultaneously(direction, nodes))


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
