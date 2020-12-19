import math
import time


def get_earliest_timestamp(filename):
    with open(filename, 'r') as f:
        for line in f:
            return int(line[:-1])


def get_buses(filename):
    with open(filename, 'r') as f:
        for line in f.readlines()[1:]:
            line = line[:-1]
            buses = line.split(',')
            return [int(bus) for bus in buses if bus != 'x']


def get_next_available(start, number):
    return (math.floor(start / number) + 1) * number


def get_next_multiples(start, numbers):
    multiples = []
    for number in numbers:
        multiples.append(get_next_available(start, number))
    return multiples


def get_raw_buses(filename):
    raw_buses = []
    with open(filename, 'r') as f:
        for line in f.readlines()[1:]:
            line = line[:-1]
            buses = line.split(',')
            for bus in buses:
                if bus.isdigit():
                    raw_buses.append(int(bus))
                else:
                    raw_buses.append(0)
    return raw_buses


def find_sequence(raw_buses, minimum):
    baseline = raw_buses[0]
    start = (math.floor(minimum / baseline) + 1) * baseline

    while True:
        if start % 100000 == 0:
            print(start)
        found_seq = True
        for idx in range(1, len(raw_buses)):
            bus = raw_buses[idx]
            if bus == 0:
                pass
            else:
                found_seq = found_seq and (start + idx) % bus == 0

            # Bail early to prevent unnecessary computation
            if not found_seq:
                break

        if found_seq:
            return start

        start += baseline


if __name__ == "__main__":
    filename = 'input.txt'
    timestamp = get_earliest_timestamp(filename)
    buses = get_buses(filename)
    multiples = get_next_multiples(timestamp, buses)

    multiple = min(multiples)
    part_one = buses[multiples.index(multiple)]
    print(f'Part One Answer: {(multiple - timestamp) * part_one}')

    raw_buses = get_raw_buses(filename)
    part_two = find_sequence(raw_buses, 100_000_000_000_000)
    print(f'Part Two Answer: {part_two}')
