import re


def xor(a, b):
    return not(a and b) and (a or b)


def part_one():
    valid_passwords = 0

    with open('input.txt') as f:
        for line in f:
            # ['1', '3', 'a', '', 'abcde', '']
            tokens = re.split('-| |:|\n', line)
            minimum = int(tokens[0])
            maximum = int(tokens[1])
            letter = tokens[2]
            password = tokens[4]

            count = 0
            for char in password:
                if char == letter:
                    count += 1

            if count >= minimum and count <= maximum:
                valid_passwords += 1

    print(f'Part One Answer: {valid_passwords}')


def part_two():
    valid_passwords = 0

    with open('input.txt') as f:
        for line in f:
            # ['1', '3', 'a', '', 'abcde', '']
            tokens = re.split('-| |:|\n', line)
            pos_a = int(tokens[0]) - 1
            pos_b = int(tokens[1]) - 1
            letter = tokens[2]
            password = tokens[4]

            a = password[pos_a] == letter
            b = password[pos_b] == letter
            valid_password = xor(a, b)

            if valid_password:
                valid_passwords += 1

    print(f'Part Two Answer: {valid_passwords}')


if __name__ == "__main__":
    part_one()
    part_two()
