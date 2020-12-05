import math


def parse_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(line[:-1])
    return data


def calculate_chars(chars, lower, upper):
    if not chars:
        return lower

    char = chars[0]
    mid = (lower + upper) / 2

    if char in ['F', 'L']:
        return calculate_chars(chars[1:], lower, math.floor(mid))
    else:
        return calculate_chars(chars[1:], math.ceil(mid), upper)


def find_positions(data):
    positions = []
    for boarding_pass in data:
        row_chars = boarding_pass[:7]
        col_chars = boarding_pass[7:]

        row = calculate_chars(row_chars, 0, 127)
        col = calculate_chars(col_chars, 0, 7)

        positions.append([row, col])
    return positions


def calculate_seat_ids(positions):
    seat_ids = []
    for position in positions:
        row = position[0]
        col = position[1]
        seat_ids.append(row * 8 + col)
    return seat_ids


def find_missing_seat_id(seat_ids):
    for seat_id in range(seat_ids[0], seat_ids[-1] + 1):
        if seat_id not in seat_ids:
            return seat_id


if __name__ == "__main__":
    data = parse_data('input.txt')
    positions = find_positions(data)
    seat_ids = calculate_seat_ids(positions)
    print(f'Part One Answer: {max(seat_ids)}')
    seat_ids.sort()
    seat_id = find_missing_seat_id(seat_ids)
    print(f'Part Two Answer: {seat_id}')
