import sys
import string


def get_data(datafile):
    with open(datafile) as f:
        data = f.read().split('\n')
        # print(f"read_data is: {read_data}")
    return data


def clean_passports(passport_data_array):
    counter = 0
    passports = {}
    for line in passport_data_array:
        # print(f"current line is: {line}")
        if not line:
            counter += 1
            # print(f"increased counter to: {counter}")
        else:
            if counter in passports.keys():
                passports[counter] = passports[counter] + ' ' + line
            else:
                passports[counter] = line
            # current_passport = line
            # if passport_data_array
        # print(f"passports current: {passports}")
    print(f"passports: \n{passports}")

    passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    passport_count = counter + 1
    print(f"number of total passports: {passport_count}")
    for passport_key in passports:
        # print(f"current_passport is: {passports[passport_key]}")
        for passport_field in passport_fields:
            if passport_field not in passports[passport_key]:
                print(f"{passports[passport_key]} is missing {passport_field}")
                passport_count -= 1
                break
        # print(f"current_passport is: {passport_key}")
        # for passport_kv in passports[passport_key].split(' '):
        #     print(f"current_passport is: {passport_kv}")

    # print(f"passport counter is: {passport_count}")

    passport_book = []
    for passport_key in passports:
        current_line = passports[passport_key]
        individual_passport = {}
        for kv in current_line.split(' '):
            print(f"kv: {kv}")
            field, value = kv.split(':')
            print(f"field: {field}, value: {value}")
            individual_passport[field] = value
        passport_book.append(individual_passport)
    print(f"passports:\n{passport_book}")

    # byr:
    #     digits: 4
    #     at least: 1920
    #     at most: 2002
    # iyr:
    #
    #
    # rules = {
    #     byr: {
    #         digits
    #     ]
    # }

    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    print(f"lets check the book")
    total_passport_count = len(passport_book)
    for passport in passport_book:
        for passport_field in passport_fields:
            if passport_field not in passport:
                # print(f"{passport} is missing {passport_field}")
                total_passport_count -= 1
                break
            elif not passport[passport_field]:
                print(f"{passport} is blank for {passport_field}")
                total_passport_count -= 1
                break
            else:
                value = passport[passport_field]
                if passport_field == 'byr':
                    if len(value) != 4 or int(value) < 1920 or int(value) > 2002:
                        # print(f"cur passport in book is: {passport}")
                        # print(f"failed {passport_field}")
                        total_passport_count -= 1
                        break
                elif passport_field == 'iyr':
                    if len(value) != 4 or int(value) < 2010 or int(value) > 2020:
                        # print(f"cur passport in book is: {passport}")
                        # print(f"failed {passport_field}")
                        total_passport_count -= 1
                        break
                elif passport_field == 'eyr':
                    if len(value) != 4 or int(value) < 2020 or int(value) > 2030:
                        # print(f"cur passport in book is: {passport}")
                        # print(f"failed {passport_field}")
                        total_passport_count -= 1
                        break
                elif passport_field == 'hgt':
                    if value[-2:] == 'cm':
                        if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                            # print(f"cur passport in book is: {passport}")
                            # print(f"failed {passport_field}")
                            total_passport_count -= 1
                            break
                    elif value[-2:] == 'in':
                        if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                            # print(f"cur passport in book is: {passport}")
                            # print(f"failed {passport_field}")
                            total_passport_count -= 1
                            break
                    else:
                        # print(f"cur passport in book is: {passport}")
                        # print(f"failed {passport_field}")
                        total_passport_count -= 1
                        break
                elif passport_field == 'hcl':
                    if value[:1] == "#":
                        for ea_char in value[1:]:
                            if ea_char not in string.hexdigits:
                                total_passport_count -= 1
                                break
                        # for ea_color in eye_colors:
                        #     if value[1:] == ea_color:
                        #         break
                    else:
                        # total_
                        # if value[:1] != "#" or all(x in string.hexdigits for x in value[1:]) == False:
                        # print(f"cur passport in book is: {passport}")
                        # print(f"failed {passport_field}")
                        total_passport_count -= 1
                        break
                elif passport_field == 'ecl':
                    if value not in eye_colors:
                        print(f"cur passport in book is: {passport}")
                        print(f"failed {passport_field}")
                        total_passport_count -= 1
                        break
                elif passport_field == 'pid':
                    if len(value) != 9 or value.isdecimal() is False:
                        print(f"cur passport in book is: {passport}")
                        print(f"failed {passport_field}")
                        total_passport_count -= 1
                        break
                # elif passport_field == 'cid':
                #     print("do nothing")


    return passport_count, total_passport_count


if __name__ == "__main__":
    # passport_data_array = get_data("testdata.txt")
    passport_data_array = get_data("data.txt")
    print(f"passport_data: {passport_data_array}")

    # passport_data_sorted = clean_passports(passport_data_array)
    cheaty_valid_passport_count, harder = clean_passports(passport_data_array)
    print(f"cheaty valid passport count: {cheaty_valid_passport_count}")
    print(f"harder check valids: {harder}")

