def get_instructions(filename):
    instructions = []
    with open(filename, 'r') as f:
        for line in f:
            line = line[:-1]
            instructions.append(line)
    return instructions


def navigate(instructions):
    orientations = ['N', 'E', 'S', 'W']
    x = 0
    y = 0
    orientation = 'E'

    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])

        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action in ['L', 'R']:
            idx = orientations.index(orientation)
            if action == 'R':
                idx = int((idx + (value / 90)) % len(orientations))
            else:
                idx = int((idx + len(orientations) - (value / 90)) %
                          len(orientations))
            orientation = orientations[idx]
        elif action == 'F':
            if orientation == 'N':
                y += value
            elif orientation == 'S':
                y -= value
            elif orientation == 'E':
                x += value
            elif orientation == 'W':
                x -= value

    return [x, y]


def convert_right_to_left(rotates):
    assert rotates < 4
    if rotates == 1:
        return 3
    elif rotates == 3:
        return 1
    return rotates


def get_quadrant(dx, dy):
    if dx >= 0:
        return 1 if dy >= 0 else 4
    else:
        return 2 if dy >= 0 else 3


def find_quadrant(dx, dy, rotates):
    quadrant = get_quadrant(dx, dy)
    return ((quadrant + (rotates - 1) + 4) % 4) + 1


def get_abs_diff(dx, dy):
    if dx >= 0:
        return [dx, dy] if dy >= 0 else[-dy, dx]
    else:
        return [dy, -dx] if dy >= 0 else [-dx, -dy]


def navigate_w_airship(instructions):
    waypoint = [10, 1]
    ship = [0, 0]

    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])

        if action == 'N':
            waypoint[1] += value
        elif action == 'S':
            waypoint[1] -= value
        elif action == 'E':
            waypoint[0] += value
        elif action == 'W':
            waypoint[0] -= value
        elif action in ['L', 'R']:
            dx = waypoint[0] - ship[0]
            dy = waypoint[1] - ship[1]

            d = get_abs_diff(dx, dy)
            ddx = d[0]
            ddy = d[1]

            rotates = int(value / 90)

            if action == 'R':
                rotates = convert_right_to_left(rotates)

            quadrant = find_quadrant(dx, dy, rotates)

            if quadrant == 1:
                waypoint = [ship[0] + abs(ddx), ship[1] + abs(ddy)]
            elif quadrant == 2:
                waypoint = [ship[0] - abs(ddy), ship[1] + abs(ddx)]
            elif quadrant == 3:
                waypoint = [ship[0] - abs(ddx), ship[1] - abs(ddy)]
            elif quadrant == 4:
                waypoint = [ship[0] + abs(ddy), ship[1] - abs(ddx)]
        elif action == 'F':
            dx = waypoint[0] - ship[0]
            dy = waypoint[1] - ship[1]

            for _ in range(value):
                ship[0] += dx
                ship[1] += dy
                waypoint[0] += dx
                waypoint[1] += dy
    return ship


if __name__ == "__main__":
    instructions = get_instructions('input.txt')
    part_one = navigate(instructions)
    print(f'Part One Answer: {abs(part_one[0]) + abs(part_one[1])}')
    part_two = navigate_w_airship(instructions)
    print(f'Part Two Answer: {abs(part_two[0]) + abs(part_two[1])}')
