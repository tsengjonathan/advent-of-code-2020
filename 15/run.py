from collections import defaultdict


def get_starting_nums(filename):
    with open(filename, 'r') as f:
        chars = f.read().split(',')
        return [int(char) for char in chars]


def last_indexes(nums, target, count):
    indexes = []
    idx = len(nums) - 1
    while len(indexes) < count:
        if nums[idx] == target:
            indexes.append(idx)
        idx -= 1
    return indexes


def play_game(starting, rounds):
    game = defaultdict(list)
    last_num = starting[-1]

    for idx in range(len(starting)):
        num = starting[idx]
        game[num].append(idx)

    idx = len(starting)
    while idx < rounds:
        if len(game[last_num]) < 2:
            last_num = 0
        else:
            last_num = game[last_num][-1] - game[last_num][-2]
        game[last_num].append(idx)
        idx += 1
    return last_num


if __name__ == "__main__":
    nums = get_starting_nums('input.txt')
    part_one = play_game(nums, 2020)
    print(f'Part One Answer: {part_one}')
    part_two = play_game(nums, 30_000_000)
    print(f'Part Two Answer: {part_two}')
