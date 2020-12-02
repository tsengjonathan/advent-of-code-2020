def part_one():
    target = 2020
    lookup = []

    with open('input.txt', 'r') as f:
        for line in f:
            num = int(line)
            remainder = target - num

            if num in lookup:
                print(f'Part One Answer: {num} * {remainder} = {num * remainder}')
                return
            else:
                lookup.append(remainder)

def part_two():
    target = 2020
    subtargets = []
    numbers = []

    with open('input.txt', 'r') as f:
        for line in f:
            num = int(line)
            numbers.append(num)
            subtargets.append(target - num)

    for subtarget in subtargets:
        lookup = []
        for num in numbers:
            remainder = subtarget - num

            if num in lookup:
                first = target - subtarget
                print(f'Part Two Answer: {num} * {remainder} * {first} = {num * remainder * first}')
                return
            else:
                lookup.append(remainder)


if __name__ == "__main__":
    part_one()
    part_two()
