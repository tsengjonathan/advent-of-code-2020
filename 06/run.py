from collections import defaultdict


def parse_any_answered(filename):
    groups = []
    with open(filename, 'r') as f:
        group = set()

        for line in f:
            line = line[:-1]
            if not line:
                groups.append(group)
                group = set()
            for answer in line:
                group.add(answer)

    groups.append(group)
    return groups


def count_answers(groups):
    count = 0
    for group in groups:
        count += len(group)
    return count


def parse_all_answered(filename):
    groups = []
    with open(filename, 'r') as f:
        members = 0
        answers = defaultdict(int)

        for line in f:
            line = line[:-1]
            if not line:
                group = []
                for answer, count in answers.items():
                    if count == members:
                        group.append(answer)
                groups.append(group)
                members = 0
                answers = defaultdict(int)
                continue
            members += 1
            for answer in line:
                answers[answer] += 1

    group = []
    for answer, count in answers.items():
        if count == members:
            group.append(answer)
    groups.append(group)
    return groups


if __name__ == "__main__":
    filename = 'input.txt'
    any_answered_groups = parse_any_answered(filename)
    part_one = count_answers(any_answered_groups)
    print(f'Part One Answer: {part_one}')
    all_answered_groups = parse_all_answered(filename)
    part_two = count_answers(all_answered_groups)
    print(f'Part Two Answer: {part_two}')
