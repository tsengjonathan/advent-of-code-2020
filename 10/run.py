def get_adapters(filename):
    adapters = []
    with open(filename, 'r') as f:
        for line in f:
            line = line[:-1]
            adapters.append(int(line))
    adapters.sort()
    return adapters


def find_jolt_diffs(adapters):
    diffs = {
        1: 0,
        2: 0,
        3: 0
    }
    last = 0

    for adapter in adapters:
        diff = adapter - last
        diffs[diff] += 1
        last = adapter

    diffs[3] += 1
    return diffs


def find_valid_next(srcIdx, adapters):
    valid_next = []
    src = adapters[srcIdx]
    for idx in range(srcIdx + 1, min(srcIdx + 4, len(adapters))):
        if adapters[idx] - src <= 3:
            valid_next.append(idx)
    return valid_next


def find_paths_helper(srcIdx, adapters, seen):
    if srcIdx == len(adapters) - 1:
        return 1

    count = 0
    valid_nexts = find_valid_next(srcIdx, adapters)
    for valid_next in valid_nexts:
        if valid_next not in seen:
            seen[valid_next] = find_paths_helper(valid_next, adapters, seen)
        count += seen[valid_next]
    return count


def find_paths(adapters):
    adapters = adapters.copy()
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)
    return find_paths_helper(0, adapters, {})


if __name__ == "__main__":
    filename = 'input.txt'
    adapters = get_adapters(filename)
    jolt_diffs = find_jolt_diffs(adapters)
    print(f'Part One Answer: {jolt_diffs[1] * jolt_diffs[3]}')
    print(f'Part Two Answer: {find_paths(adapters)}')
