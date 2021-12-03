import AoC_tools as AT


req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
opt_fields = ['cid']


def quick_validation(data):
    valid_passports = 0

    for entry in data:
        # check that each required field is in each entry
        contained_fields = [req_field in entry for req_field in req_fields]
        if False in contained_fields:
            continue
        else:
            valid_passports += 1

    return valid_passports


def get_field(label, entry):
    # extracts the field value

    # starts after 3 char label and colon
    start = entry.find(label) + 4

    # ends with space, new line, or end of string
    sp_end = entry[start:].find(' ')
    nl_end = entry[start:].find('\n')
    if sp_end < 0 and nl_end < 0:
        end = start + 10
    elif sp_end < 0:
        end = nl_end
    elif nl_end < 0:
        end = sp_end
    else:
        end = min(sp_end, nl_end)
    end += start

    field = entry[start:end]
    return field


def detailed_validation(data):
    valid_passports = 0
    for entry in data:

        # quick check that all required fields are present
        contained_fields = [req_field in entry for req_field in req_fields]
        if False in contained_fields:
            continue

        # validate birth year, else continue
        byr = get_field('byr', entry)
        if len(byr) != 4:
            continue
        byr = int(byr)
        if not (1920 <= byr <= 2002):
            continue

        # validate issue year, else continue
        iyr = get_field('iyr', entry)
        if len(iyr) != 4:
            continue
        iyr = int(iyr)
        if not (2010 <= iyr <= 2020):
            continue

        # validate expiration year, else continue
        eyr = get_field('eyr', entry)
        if len(eyr) != 4:
            continue
        eyr = int(eyr)
        if not (2020 <= eyr <= 2030):
            continue

        # validate height, else continue
        hgt_full = get_field('hgt', entry)
        if len(hgt_full) < 4:
            continue
        unit = hgt_full[-2:]
        hgt = int(hgt_full[:-2])

        # criteria is based on unit
        if unit == 'cm':
            if not (150 <= hgt <= 193):
                continue
        elif unit == 'in':
            if not (59 <= hgt <= 76):
                continue
        else:
            continue

        # validate hair color, else continue
        alphanum = 'abcdefghijklmnopqrstuvwxyz0123456789'
        hcl = get_field('hcl', entry)
        if len(hcl) < 7:
            continue

        # hash is necessary; check length
        if not hcl[0] == '#':
            continue
        else:
            hcl = hcl[1:]
        if not len(hcl) == 6:
            continue

        # check each char is valid
        valid_hcl = True
        for char in hcl:
            if char not in alphanum:
                valid_hcl = False
                break
        if not valid_hcl:
            continue

        # validate eye color, else continue
        ecl = get_field('ecl', entry)
        if len(ecl) != 3:
            continue
        if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue

        # validate passport id, else continue
        pid = get_field('pid', entry)
        if len(pid) != 9:
            continue
        valid_pid = True
        for char in pid:
            if char not in '0123456789':
                valid_pid = False
                break
        if not valid_pid:
            continue

        valid_passports += 1

    return valid_passports


def part_one(input_data):
    res = quick_validation(input_data)
    print("\nnumber of valid passports: ", res)


def part_two(input_data):
    res = detailed_validation(input_data)
    print("\nnumber of valid passports: ", res)


def both(input_data):
    res = quick_validation(input_data)
    print("\nnumber of valid passports: ", res)
    res = detailed_validation(input_data)
    print("number of valid passports: ", res)


if __name__ == '__main__':
    # entries are separated by double line breaks
    data = AT.load_txt(input("please enter data path: \n"), sep='\n\n')
    res = quick_validation(data)
    print("\npart one number of valid passports: ", res)
    res = detailed_validation(data)
    print("part two number of valid passports: ", res)

