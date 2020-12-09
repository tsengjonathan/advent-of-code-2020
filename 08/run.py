from instruction import Instruction


def get_instructions(filename):
    instructions = []
    with open(filename, 'r') as f:
        for line in f:
            tokens = line[:-1].split(' ')
            assert len(tokens) == 2
            instruction = Instruction(tokens[0], int(tokens[1]))
            instructions.append(instruction)
    return instructions


def boot_code(instructions, track_visited=True):
    acc = 0
    step = 0

    while step < len(instructions):
        instruction = instructions[step]

        if instruction.visited:
            return acc

        if instruction.op == 'acc':
            acc += instruction.arg
            step += 1
        elif instruction.op == 'jmp':
            step += instruction.arg
        elif instruction.op == 'nop':
            step += 1
        else:
            raise RuntimeError(f'Unseen op {instruction.op} at step {step}')

        instruction.visited = True

    return acc


def reset_instructions(instructions):
    for instruction in instructions:
        instruction.reset()


def find_possible_changes(instructions):
    candidates = []
    step = 0

    while step < len(instructions):
        instruction = instructions[step]

        if instruction.visited:
            break

        if instruction.op == 'acc':
            step += 1
        elif instruction.op == 'jmp':
            step += instruction.arg
            if instruction.arg != 0:
                candidates.append(instruction)
        elif instruction.op == 'nop':
            step += 1
            if instruction.arg != 0:
                candidates.append(instruction)
        else:
            raise RuntimeError(f'Unseen op {instruction.op} at step {step}')

        instruction.visited = True

    reset_instructions(instructions)
    return candidates


def has_infinite_loop(instructions):
    step = 0

    while step < len(instructions):
        instruction = instructions[step]

        if instruction.visited:
            return True

        if instruction.op == 'acc':
            step += 1
        elif instruction.op == 'jmp':
            step += instruction.arg
        elif instruction.op == 'nop':
            step += 1
        else:
            raise RuntimeError(f'Unseen op {instruction.op} at step {step}')

        instruction.visited = True

    return False


def try_candidates(instructions, candidates):
    for candidate in candidates:
        candidate.op = 'nop' if candidate.op == 'jmp' else 'jmp'

        loop = has_infinite_loop(instructions)
        reset_instructions(instructions)
        if not loop:
            candidate.op = 'nop' if candidate.op == 'jmp' else 'jmp'
            return boot_code(instructions, track_visited=False)

    return None


if __name__ == "__main__":
    filename = 'input.txt'
    instructions = get_instructions(filename)
    part_one = boot_code(instructions)
    print(f'Part One Answer: {part_one}')
    reset_instructions(instructions)
    candidates = find_possible_changes(instructions)
    part_two = try_candidates(instructions, candidates)
    print(f'Part Two Answer: {part_two}')
