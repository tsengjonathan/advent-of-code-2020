def get_numbers(filename):
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            line = line[:-1]
            numbers.append(int(line))
    return numbers


def has_pair(number, candidates):
    buffer = []
    for candidate in candidates:
        if candidate in buffer:
            return True
        need = number - candidate
        buffer.append(need)
    return False


def find_invalid_number(numbers, preamble):
    idx = preamble

    while idx < len(numbers):
        number = numbers[idx]
        candidates = numbers[idx - preamble:idx]
        if not has_pair(number, candidates):
            return number
        idx += 1


def find_contiguous_set(target, numbers, startIdx):
    total = 0
    for idx in range(startIdx, len(numbers)):
        number = numbers[idx]
        total += number
        if total > target:
            return find_contiguous_set(target, numbers, startIdx + 1)
        elif total == target and numbers[startIdx] != number:
            endIdx = idx + 1
            return numbers[startIdx:endIdx]


if __name__ == "__main__":
    filename = 'input.txt'
    numbers = get_numbers(filename)
    part_one = find_invalid_number(numbers, 25)
    print(f'Part One Answer: {part_one}')
    contiguous_set = find_contiguous_set(part_one, numbers, 0)
    part_two = min(contiguous_set) + max(contiguous_set)
    print(f'Part Two Answer: {part_two}')
