import sys
from icecream import ic
import heapq

# import argparse

# parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
# parser.add_argument(i'file', '--file'. help='please give me a file to read from')
# args = parser.parse_args()


# def data_array(input_file="test-data.txt"):
def data_array(input_file="data.txt"):
    with open(input_file) as f:
        content = f.read().split('\n')
        # ic(content)

        final_dict = {}
        cur_elf = 1
        for line in content:
            # ic(line)
            if line == '':
                cur_elf += 1
                continue
            if cur_elf in final_dict.keys():
                final_dict[cur_elf].append(line)
                # ic(final_dict)
            else:
                final_dict[cur_elf] = [line]
                # ic(final_dict)
        # ic(final_dict)
        # exit()
    f.close()
    return final_dict


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


def main():
    data = data_array()
    # test a subset
    # data = data[:5]
    # data.append(479)
    # print(f"expenses = {expenses}")

    total_calories_per_elf = get_calories_per_elf(data)
    # ic(total_calories_per_elf)

    # get_elf_with_highest_calories(total_calories_per_elf)
    get_highest_calories(total_calories_per_elf)

    get_three_highest_calories(total_calories_per_elf)

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
