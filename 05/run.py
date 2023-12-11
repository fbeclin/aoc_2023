from enum import Enum
import regex as re

seed2soil_map = []
soil2fertilizer_map = []
fertilizer2water_map = []
water2light_map = []
light2temperature_map = []
temperature2humidity_map = []
humidity2location_map = []


def findNumberInMap(number: int, map: []) -> int:
    for m in map:
        if number >= m[1] and number <= m[1] + m[2]:
            return m[0] + abs(m[1] - number)
    return number


def getLocationForSeed(seed: int) -> int:
    soil = findNumberInMap(seed, seed2soil_map)
    fertilizer = findNumberInMap(soil, soil2fertilizer_map)
    water = findNumberInMap(fertilizer, fertilizer2water_map)
    light = findNumberInMap(water, water2light_map)
    temperature = findNumberInMap(light, light2temperature_map)
    humidity = findNumberInMap(temperature, temperature2humidity_map)
    return findNumberInMap(humidity, humidity2location_map)


def run1(filename: str):
    seeds = []
    map_to_fill = []

    with open(filename) as file:
        for line in enumerate(file):
            if line[0] == 0:
                seeds = list(
                    map(
                        lambda x: int(x),
                        re.findall("\d+", line[1].rstrip().split(":")[1]),
                    )
                )
            else:
                command = line[1].rstrip()
                if command != "":
                    match command:
                        case "seed-to-soil map:":
                            map_to_fill = seed2soil_map
                        case "soil-to-fertilizer map:":
                            map_to_fill = soil2fertilizer_map
                        case "fertilizer-to-water map:":
                            map_to_fill = fertilizer2water_map
                        case "water-to-light map:":
                            map_to_fill = water2light_map
                        case "light-to-temperature map:":
                            map_to_fill = light2temperature_map
                        case "temperature-to-humidity map:":
                            map_to_fill = temperature2humidity_map
                        case "humidity-to-location map:":
                            map_to_fill = humidity2location_map
                        case _:
                            map_to_fill.append(
                                list(map(lambda x: int(x), re.findall("\d+", command)))
                            )

    print(min([getLocationForSeed(seed) for seed in seeds]))


def run2(filename: str):
    seeds = []
    map_to_fill = []

    with open(filename) as file:
        for line in enumerate(file):
            if line[0] == 0:
                seeds = list(
                    map(
                        lambda x: int(x),
                        re.findall("\d+", line[1].rstrip().split(":")[1]),
                    )
                )
            else:
                command = line[1].rstrip()
                if command != "":
                    match command:
                        case "seed-to-soil map:":
                            map_to_fill = seed2soil_map
                        case "soil-to-fertilizer map:":
                            map_to_fill = soil2fertilizer_map
                        case "fertilizer-to-water map:":
                            map_to_fill = fertilizer2water_map
                        case "water-to-light map:":
                            map_to_fill = water2light_map
                        case "light-to-temperature map:":
                            map_to_fill = light2temperature_map
                        case "temperature-to-humidity map:":
                            map_to_fill = temperature2humidity_map
                        case "humidity-to-location map:":
                            map_to_fill = humidity2location_map
                        case _:
                            map_to_fill.append(
                                list(map(lambda x: int(x), re.findall("\d+", command)))
                            )

    print(
        min(
            [
                getLocationForSeed(seed)
                for i in range(0, len(seeds), 2)
                for seed in range(seeds[i], seeds[i] + seeds[i + 1])
            ]
        )
    )


if __name__ == "__main__":
    filename = "sample.txt"
    # filename = "input.txt"
    # run1(filename)
    run2(filename)
