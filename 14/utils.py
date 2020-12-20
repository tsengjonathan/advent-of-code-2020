MAX_LEN = 36


def decimal_to_bits(decimal):
    tmp = decimal
    bits = [0] * MAX_LEN
    for idx in range(MAX_LEN):
        power = MAX_LEN - idx - 1
        if 2 ** power <= tmp:
            bits[idx] = 1
            tmp -= 2 ** power
    return bits


def bits_to_decimal(bits):
    decimal = 0
    for idx in range(MAX_LEN):
        bit = bits[idx]
        power = MAX_LEN - idx - 1
        if bit == 1:
            decimal += 2 ** power
    return decimal
