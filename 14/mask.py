import random
from collections import defaultdict

from utils import MAX_LEN, decimal_to_bits, bits_to_decimal


class Mask:
    def __init__(self, data):
        raw = data.split(' = ')[1]
        mask = []

        for char in raw:
            if char == 'X':
                mask.append(-1)
            else:
                mask.append(int(char))

        self.mask = mask
        self.mems = []

    def apply_v1(self, mem):
        masked = mem.copy()
        for idx in range(MAX_LEN):
            if self.mask[idx] >= 0:
                masked[idx] = self.mask[idx]
        return masked

    def add_mem(self, data):
        tokens = data.split(' = ')
        address = int(''.join([char for char in tokens[0] if char.isdigit()]))

        bits = [int(bit) for bit in decimal_to_bits(int(tokens[1]))]

        while len(bits) < MAX_LEN:
            bits.insert(0, 0)

        self.mems.append([address, bits])

    def apply_v2(self, mem):
        address = mem[0]
        bits = mem[1]

        masked = decimal_to_bits(address)
        for idx in range(MAX_LEN):
            if self.mask[idx] == 1:
                masked[idx] = 1
            elif self.mask[idx] == -1:
                masked[idx] = -1

        count = 2 ** masked.count(-1)
        combinations = set()
        while len(combinations) < count:
            combination = [random.choice(
                ['0', '1']) if e == -1 else str(e) for e in masked]
            combinations.add(''.join(combination))

        addresses = defaultdict(int)
        for combination in combinations:
            addr_bits = [int(e) for e in combination]
            addresses[bits_to_decimal(addr_bits)] = bits
        return dict(addresses)

    def __repr__(self):
        return f'mask: {self.mask}, mems: {self.mems}'
