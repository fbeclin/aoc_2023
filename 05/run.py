import datetime
import regex as re

seed2soil_map = []
soil2fertilizer_map = []
fertilizer2water_map = []
water2light_map = []
light2temperature_map = []
temperature2humidity_map = []
humidity2location_map = []

# part 2
memo = {}


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


def sortMapBySource(map: []):
    map.sort(key=lambda x: x[1])


def sortMaps():
    sortMapBySource(seed2soil_map)
    sortMapBySource(soil2fertilizer_map)
    sortMapBySource(fertilizer2water_map)
    sortMapBySource(water2light_map)
    sortMapBySource(light2temperature_map)
    sortMapBySource(temperature2humidity_map)
    sortMapBySource(humidity2location_map)


def getNewRange(start: int, end: int, map: []) -> []:
    for i, m in enumerate(map):
        print(f"map: {m}")
        m_max = m[1] + m[2]
        m_diff = m[0] - m[1]
        if start < m_max:
            if start < m[1]:
                break
            print(f"{start} < {m_max}")
            # new_start = start + m_diff
            if end < m_max:
                # found new range
                return [[start + m_diff, end + m_diff]]
            else:
                # split range
                return [[start + m_diff, m_max - 1 + m_diff]] + getNewRange(
                    m_max, end, map[i + 1 :]
                )

    return [[start, end]]


def getMinLocationForSeedRange(seedRanges: []) -> int:
    soilRanges = []
    for range in seedRanges:
        soilRanges += getNewRange(range[0], range[1], seed2soil_map)

    fertilizerRanges = []
    for range in soilRanges:
        fertilizerRanges += getNewRange(range[0], range[1], soil2fertilizer_map)

    waterRanges = []
    for range in fertilizerRanges:
        waterRanges += getNewRange(range[0], range[1], fertilizer2water_map)

    lightRanges = []
    for range in waterRanges:
        lightRanges += getNewRange(range[0], range[1], water2light_map)

    tempRanges = []
    for range in lightRanges:
        tempRanges += getNewRange(range[0], range[1], light2temperature_map)

    humidityRanges = []
    for range in tempRanges:
        humidityRanges += getNewRange(range[0], range[1], temperature2humidity_map)

    locationRanges = []
    for range in humidityRanges:
        locationRanges += getNewRange(range[0], range[1], humidity2location_map)
    return min(locationRanges, key=lambda x: x[0])[0]


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
    sortMaps()
    print(
        getMinLocationForSeedRange(
            [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
        )
    )


if __name__ == "__main__":
    # get the start datetime
    st = datetime.datetime.now()
    filename = "sample.txt"
    # filename = "input.txt"
    # run1(filename)
    run2(filename)

    # get the end datetime
    et = datetime.datetime.now()

    # get execution time
    elapsed_time = et - st
    print("Execution time:", elapsed_time, "seconds")
