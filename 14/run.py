from collections import defaultdict

from mask import Mask
from utils import bits_to_decimal


def get_program(filename):
    program = []
    mask = None
    with open(filename, 'r') as f:
        for line in f:
            line = line[:-1]
            if 'mask' in line:
                if mask is not None:
                    program.append(mask)
                mask = Mask(line)
            elif 'mem' in line:
                mask.add_mem(line)
        program.append(mask)
    return program


def run_program_v1(program):
    addresses = defaultdict(int)

    for mask in program:
        for mem in mask.mems:
            address = mem[0]
            bits = mem[1]
            masked = mask.apply_v1(bits)
            addresses[address] = masked
    return addresses


def run_program_v2(program):
    addresses = defaultdict(int)
    for mask in program:
        for mem in mask.mems:
            subaddresses = mask.apply_v2(mem)
            addresses.update(subaddresses)
    return addresses


if __name__ == "__main__":
    program = get_program('input.txt')
    addresses_v1 = run_program_v1(program)
    part_one = sum([bits_to_decimal(bits) for bits in addresses_v1.values()])
    print(f'Part One Answer: {part_one}')
    addresses_v2 = run_program_v2(program)
    part_two = sum([bits_to_decimal(bits) for bits in addresses_v2.values()])
    print(f'Part Two Answer: {part_two}')
