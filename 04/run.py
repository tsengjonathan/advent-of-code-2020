def parse_data(filename):
    data = []
    buffer = {}

    with open(filename, 'r') as f:
        for line in f:
            line = line[:-1]
            if not line:
                data.append(buffer)
                buffer = {}

            fields = line.split()
            for field in fields:
                pair = field.split(':')
                assert len(pair) == 2
                buffer[pair[0]] = pair[1]

    # Append the latest set of data
    data.append(buffer)
    return data

def part_one(passports):
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid_passports = []
    for passport in passports:
        if not required_fields.difference(set(passport.keys())):
            valid_passports.append(passport)
    return valid_passports


def part_two(passports):
    count = 0
    for passport in passports:
        valid = True
        for key, value in passport.items():
            if key == 'byr':
                if not value.isdigit():
                    valid = False
                    break
                birth_year = int(value)
                valid = valid and birth_year >= 1920 and birth_year <= 2002
            elif key == 'iyr':
                if not value.isdigit():
                    valid = False
                    break
                issue_year = int(value)
                valid = valid and issue_year >= 2010 and issue_year <= 2020
            elif key == 'eyr':
                if not value.isdigit():
                    valid = False
                    break
                exp_year = int(value)
                valid = valid and exp_year >= 2020 and exp_year <= 2030
            elif key == 'hgt':
                if len(value) < 4 or len(value) > 5 or not value[:-2].isdigit():
                    valid = False
                    break
                unit = value[-2:]
                height = int(value[:-2])

                if unit == 'cm':
                    valid = valid and height >= 150 and height <= 193
                elif unit == 'in':
                    valid = valid and height >= 59 and height <= 76
                else:
                    valid = False   
            elif key == 'hcl':
                valid = valid and len(value) == 7 and value[0] == '#'
                for char in value[1:]:
                    valid = valid and (char.isdigit() or char in ['a', 'b', 'c', 'd', 'e', 'f'])
            elif key == 'ecl':
                valid = valid and value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            elif key == 'pid':
                valid = valid and len(value) == 9
                for digit in value:
                    valid = valid and digit.isdigit()

        count += 1 if valid else 0
    return count

if __name__ == "__main__":
    passports = parse_data('input.txt')
    part_one = part_one(passports)
    print(f'Part One Answer: {len(part_one)}')
    print(f'Part Two Answer: {part_two(part_one)}')
