import sys
import argparse
from icecream import ic

# import heapq

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-r", "--real", action="store_true", help="whether to run with real data"
)
# parser.add_argument(i'file', '--file'. help='please give me a file to read from')
args = parser.parse_args()


def data_array(input_file="test-data.txt"):
    # def data_array(input_file="data.txt"):
    with open(input_file) as f:
        content = f.read().split("\n")
        # ic(content)

        # final_dict = {}
        # cur_elf = 1
        # for line in content:
        #     # ic(line)
        #     if line == '':
        #         cur_elf += 1
        #         continue
        #     if cur_elf in final_dict.keys():
        #         final_dict[cur_elf].append(line)
        #         # ic(final_dict)
        #     else:
        #         final_dict[cur_elf] = [line]
        #         # ic(final_dict)
        # # ic(final_dict)
        # # exit()
    f.close()
    return content
    # return final_dict


def get_calories_per_elf(data):
    calories_per_elf = {}
    for elf in data.keys():
        calories_per_elf[elf] = 0
        for item in data[elf]:
            calories_per_elf[elf] += int(item)
    # ic()
    return calories_per_elf


def get_elf_with_highest_calories(calories_per_elf):
    ic(max(calories_per_elf, key=calories_per_elf.get))
    # ic(max(calories_per_elf))
    exit()
    return elf_with_highest_calories


def get_highest_calories(calories_per_elf):
    # highest =
    highest = max(calories_per_elf.values())
    ic(highest)
    return


def get_three_highest_calories(calories_per_elf):
    highest_three = heapq.nlargest(3, calories_per_elf.values())
    ic(highest_three)
    highest_three_total = sum(highest_three)
    ic(highest_three_total)
    return


def part_one(input_data):
    calibration_values = []

    # ic(input_data)

    [
        calibration_values.append(
            "".join([number for number in value if number.isdigit()])
        )
        for value in input_data
    ]

    # calibration_values_two = [print(value[0], value[-1]) for value in calibration_values]
    # calibration_values_two = [str(value[0]).join(str(value[-1])) for value in calibration_values]
    calibration_values_two = [
        int(f"{value[0]}{value[-1]}") for value in calibration_values
    ]
    # ic(calibration_values)
    # ic(calibration_values_two)

    print(f"sum: {sum(calibration_values_two)}")

    return


def part_two(input_data):
    calibration_values = []

    # ic(input_data)

    # numbers_spelled_out = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    # numbers_spelled_out = {
    #     "one": 1,
    #     "two": 2,
    #     "three": 3,
    #     "four": 4,
    #     "five": 5,
    #     "six": 6,
    #     "seven": 7,
    #     "eight": 8,
    #     "nine": 9,
    # }

    teens = {
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }

    doubledigits = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    numbers_spelled_out = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        0: "zero",
    }

    converted_data = []


    # for line in input_data:
    #     length = len(line)

    #     ic(line)
    #     for char_num in range(length):
    #         # ic(char_num)
    #         left_to_right = line[:char_num+1]
    #         # ic(line[:char_num+1])
    #         ic(left_to_right)

    #         if left_to_right in teens.values():
    #             print("idk")
    #     sys.exit()



    for line in input_data:
        ic(line)
        converted_line = line

        for key, value in teens.items():
            if value in line:
                converted_line = converted_line.replace(value, value[0]+str(key)+value[-1])
                # ic(converted_line)

        for key, value in doubledigits.items():
            if value in line:
                for s_key, s_value in numbers_spelled_out.items():
                    if value+s_value in line:
                        ic(f"{value+s_value} in {line}")
                        converted_line = converted_line.replace(value+s_value, value[0]+str(key + s_key)+s_value[-1])
                        # ic(converted_line)
        
        for key, value in doubledigits.items():
            if value in line:
                converted_line = converted_line.replace(value, value[0]+str(key)+value[-1])
                # ic(converted_line)
        
        for key, value in numbers_spelled_out.items():
            # TODO: need to handle this better
            if value in line:
                converted_line = converted_line.replace(value, value[0]+str(key)+value[-1])
                ic(converted_line)

        converted_line = [char for char in converted_line if char.isdigit()]
        ic(converted_line)



        # for key, value in numbers_spelled_out.items():
        #     #    ic(key, value)
        #     if value in line:
        #         ic(f"{value} is in {line}; should be {key}")
        #         converted_line = converted_line.replace(value, str(key))
        #         ic(converted_line)
        # #    converted_data.append(line.replace(key, str(value)))
        converted_data.append(converted_line)
    ic(converted_data)




    calibration_values = []

    # ic(input_data)

    [
        calibration_values.append(
            "".join([number for number in value if number.isdigit()])
        )
        for value in converted_data
    ]

    # calibration_values_two = [print(value[0], value[-1]) for value in calibration_values]
    # calibration_values_two = [str(value[0]).join(str(value[-1])) for value in calibration_values]
    calibration_values_two = [
        int(f"{value[0]}{value[-1]}") for value in calibration_values
    ]
    # ic(calibration_values)
    # ic(calibration_values_two)

    print(f"sum: {sum(calibration_values_two)}")



    # calibration_values = 

    # for value in input_data:
    # decoded_value = [value.replace() ]

    # [calibration_values.append(''.join([number for number in value if number.isdigit()])) for value in input_data]

    # calibration_values_two = [print(value[0], value[-1]) for value in calibration_values]
    # calibration_values_two = [str(value[0]).join(str(value[-1])) for value in calibration_values]
    # calibration_values_two = [int(f"{value[0]}{value[-1]}") for value in calibration_values]
    # ic(calibration_values)
    # ic(calibration_values_two)

    # print(f"sum: {sum(calibration_values_two)}")

    return


def main():
    if args.real:
        data = data_array("data.txt")
    else:
        data = data_array("test-data.txt")
    # test a subset
    # data = data[:5]
    # data.append(479)
    # print(f"expenses = {expenses}")

    # total_calories_per_elf = get_calories_per_elf(data)
    # # ic(total_calories_per_elf)

    # # get_elf_with_highest_calories(total_calories_per_elf)
    # get_highest_calories(total_calories_per_elf)

    # get_three_highest_calories(total_calories_per_elf)

    # part_one(data)

    part_two(data)

    ic()

    # exit()

    # number_increased = find_increased_count(data)
    # print(f"increased count: {number_increased}")

    # number_increased_windows = increased_count_windows(data)
    # print(f"increased count windows: {number_increased_windows}")

    # pairs = find_2020_pairs(expenses)
    # print(f"products for 2 expenses that sum to 2020: {pairs}")

    # triples = find_2020_triples(expenses)
    # print(f"products for 3 expenses that sum to 2020: {triples}")

    return


if __name__ == "__main__":
    ic()
    # parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
    # parser.add_argument('--file', '-f', dest='file', help='please give me a file to read from')
    # parser.add_argument('--verbose', '-v', action='count', help='let me know if you want to see more details')
    # args = parser.parse_args()
    # print(dup_finder(args.file, args.verbose, 0))
    # print(file_duplicator(args.file, args.verbose, 0))

    main()
