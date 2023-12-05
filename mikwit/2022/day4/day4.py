import sys
from icecream import ic
import click
from itertools import islice
# import heapq

# import argparse

# parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
# parser.add_argument(i'file', '--file'. help='please give me a file to read from')
# args = parser.parse_args()

import string

# ic()

priority_index_array = list(string.ascii_lowercase) + list(string.ascii_uppercase)
# ic(priority_index_array)


# def data_array(input_file="test-data.txt"):
def data_array(input_file="data.txt"):
    with open(input_file) as f:
        content = f.read().split('\n')
        # ic(content)
    f.close()
    return content
    # return final_dict


def get_priority(value):
    priority = priority_index_array.index(value) + 1
    return priority


def get_shared(data):
    item_priority_sum = 0
    for line in data:
        half = len(line)//2
        firsthalf, secondhalf = line[:half], line[half:]
        item = list(set(firsthalf).intersection(set(secondhalf)))
        # ic(common)
        item_priority = get_priority(item[0])
        item_priority_sum += item_priority
    ic(item_priority_sum)
    return


def get_badges(data):
    badge_priority_sum = 0
    for x in (data[i:i + 3] for i in range(0, len(data), 3)):
        # ic(x)
        badge = list(set(x[0]).intersection(set(x[1])).intersection(set(x[2])))
        # ic(badge)
        badge_priority = get_priority(badge[0])
        badge_priority_sum += badge_priority
    ic(badge_priority_sum)
    return
        

def convert_to_set(shorthand):
    shorthand_start, shorthand_end = shorthand.split('-')
    # ic(shorthand_start, shorthand_end)
    range_set = set(range( int(shorthand_start), int(shorthand_end) + 1 )  )
    return range_set


def part_one(data):
    """In how many pairs (lines) does one range fully contain the other?"""
    # set(two).intersection(set(one))

    pair_count = 0

    for line in data:
        pair_one, pair_two = line.split(',')
        # pair_one_range = set(range( int(pair_one[0]), int(pair_one[2]) + 1 )  )
        pair_one_range = convert_to_set(pair_one)
        pair_two_range = convert_to_set(pair_two)
        # ic(pair_one_range, pair_two_range)

        if pair_one_range.issubset(pair_two_range):
            pair_count += 1
        elif pair_two_range.issubset(pair_one_range):
            pair_count += 1

        # exit()
    ic(pair_count)
    return


def part_two(data):
    """In how many pairs (lines) does one range overlap the other?"""
    overlap_pair_count = 0
    for line in data:
        pair_one, pair_two = line.split(',')
        pair_one_range = convert_to_set(pair_one)
        pair_two_range = convert_to_set(pair_two)

        # ic(pair_one_range.intersection(pair_two_range))
        # ic(pair_two_range.intersection(pair_one_range))

        if pair_one_range.intersection(pair_two_range):
            overlap_pair_count += 1
        # elif pair_two_range.issubset(pair_one_range):
            # pair_count += 1

        # exit()
    ic(overlap_pair_count)
    return


@click.command()
@click.argument('file')
def main(file):
    data = data_array(file)
    # ic(data)
    # exit()

    part_one(data)

    part_two(data)

    # get_total_score(data)
    # shared = get_shared(data)

    # badges = get_badges(data)
    # ic()

    return


if __name__ == "__main__":
    # ic()
    # parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
    # parser.add_argument('--file', '-f', dest='file', help='please give me a file to read from')
    # parser.add_argument('--verbose', '-v', action='count', help='let me know if you want to see more details')
    # args = parser.parse_args()
    # print(dup_finder(args.file, args.verbose, 0))
    # print(file_duplicator(args.file, args.verbose, 0))
    ic()
    main()
    ic()