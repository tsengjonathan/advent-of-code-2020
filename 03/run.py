
def parse_input(filename):
    puzzle = []
    with open(filename, 'r') as f:
        for line in f:
            row = [char for char in line]
            puzzle.append(row[:-1])
    return puzzle


def solve_puzzle(puzzle, x_delta, y_delta):
    x = 0
    y = 0

    tree_count = 0

    while y < len(puzzle):
        tree_count += 1 if puzzle[y][x] == '#' else 0

        y += y_delta
        x = (x + x_delta) % len(puzzle[0])

    return tree_count


if __name__ == "__main__":
    puzzle = parse_input('input.txt')
    three_one = solve_puzzle(puzzle, 3, 1)
    print(f'Part One Answer: {three_one}')

    one_one = solve_puzzle(puzzle, 1, 1)
    five_one = solve_puzzle(puzzle, 5, 1)
    seven_one = solve_puzzle(puzzle, 7, 1)
    one_two = solve_puzzle(puzzle, 1, 2)
    part_two = three_one * one_one * five_one * seven_one * one_two
    print(f'Part Two Answer: {part_two}')


