def get_layout(filename):
    layout = []
    with open(filename, 'r') as f:
        for line in f:
            line = line[:-1]
            layout.append([seat for seat in line])
    return layout


def init_layout(layout):
    new_layout = []
    for row in layout:
        new_layout.append([None for _ in row])
    return new_layout


def get_adjacent(row, col, layout):
    adjacents = []
    if row > 0:
        adjacents.append(layout[row - 1][col])
        if col > 0:
            adjacents.append(layout[row - 1][col - 1])
        if col < len(layout[0]) - 1:
            adjacents.append(layout[row - 1][col + 1])
    if row < len(layout) - 1:
        adjacents.append(layout[row + 1][col])
        if col > 0:
            adjacents.append(layout[row + 1][col - 1])
        if col < len(layout[0]) - 1:
            adjacents.append(layout[row + 1][col + 1])
    if col > 0:
        adjacents.append(layout[row][col - 1])
    if col < len(layout[0]) - 1:
        adjacents.append(layout[row][col + 1])
    return adjacents


def get_line_of_sight(row, col, layout):
    los = []

    idx = row - 1
    while idx >= 0:
        pos = layout[idx][col]
        if pos in ['#', 'L']:
            los.append(pos)
            break
        idx -= 1

    idx = row + 1
    while idx < len(layout):
        pos = layout[idx][col]
        if pos in ['#', 'L']:
            los.append(pos)
            break
        idx += 1

    idx = col - 1
    while idx >= 0:
        pos = layout[row][idx]
        if pos in ['#', 'L']:
            los.append(pos)
            break
        idx -= 1

    idx = col + 1
    while idx < len(layout[0]):
        pos = layout[row][idx]
        if pos in ['#', 'L']:
            los.append(pos)
            break
        idx += 1

    x = col - 1
    y = row - 1
    while x >= 0 and y >= 0:
        pos = layout[y][x]
        if pos in ['#', 'L']:
            los.append(pos)
            break
        x -= 1
        y -= 1

    x = col + 1
    y = row - 1
    while x < len(layout[0]) and y >= 0:
        pos = layout[y][x]
        if pos in ['#', 'L']:
            los.append(pos)
            break
        x += 1
        y -= 1

    x = col - 1
    y = row + 1
    while x >= 0 and y < len(layout):
        pos = layout[y][x]
        if pos in ['#', 'L']:
            los.append(pos)
            break
        x -= 1
        y += 1

    x = col + 1
    y = row + 1
    while x < len(layout[0]) and y < len(layout):
        pos = layout[y][x]
        if pos in ['#', 'L']:
            los.append(pos)
            break
        x += 1
        y += 1

    return los


def run_round(layout, strategy, minimum):
    new_layout = init_layout(layout)
    row = 0
    col = 0
    while row < len(layout):
        position = layout[row][col]
        adjacents = strategy(row, col, layout)
        if position == 'L' and adjacents.count('#') == 0:
            new_layout[row][col] = '#'
        elif position == '#' and adjacents.count('#') >= minimum:
            new_layout[row][col] = 'L'
        else:
            new_layout[row][col] = position

        col += 1
        if col == len(layout[0]):
            row += 1
            col = 0
    return new_layout


def check_equal(a, b):
    is_equal = True
    for idx in range(len(a)):
        is_equal = is_equal and a[idx] == b[idx]
    return is_equal


def run_indefinitely(layout, strategy, minimum):
    before = layout
    after = run_round(layout, strategy, minimum)

    while not check_equal(before, after):
        before = after
        after = run_round(before, strategy, minimum)

    return after


def count_occurrences(layout, type):
    count = 0
    for row in layout:
        count += row.count(type)
    return count


if __name__ == "__main__":
    layout = get_layout('input.txt')
    part_one = run_indefinitely(layout, get_adjacent, 4)
    print(f'Part One Answer: {count_occurrences(part_one, "#")}')
    part_two = run_indefinitely(layout, get_line_of_sight, 5)
    print(f'Part Two Answer: {count_occurrences(part_two, "#")}')
