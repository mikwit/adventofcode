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
    
    f.close()
    
    return content

    # return final_dict


def parse_data_lines(data):

    instructions = []
    box_rows_top_to_bottom = []
    key = []
    num_of_stacks = ""
    stacks = {}

    for line in data:
        if line == "":
            continue
        elif line.startswith("move"):
            instructions.append(line)
        elif line[1].isdigit():
            # key.append(line)
            num_of_stacks = line
            # key = [char for char in line if char.isdigit()]
        else:
            box_rows_top_to_bottom.append(line)
            # print(f"{line=}")
    
    box_rows_bottom_to_top = box_rows_top_to_bottom.copy()
    box_rows_bottom_to_top.reverse()

    # ic(box_rows_top_to_bottom)
    # ic(box_rows_bottom_to_top)
    # ic(num_of_stacks)
    # ic(instructions)

    for char in num_of_stacks:
        if char.isdigit():
            # ic(num_of_stacks.index(char))
            # key.append(num_of_stacks.index(char))
            # key.append(char)

            cur_key = num_of_stacks.index(char)
            # ic(cur_key)
            key.append(cur_key)

            for row in box_rows_bottom_to_top:
                cur_box = row[cur_key]
                # ic(cur_box)
                if cur_box == ' ':
                    continue
                # ic(char in stacks.keys())
                if char in stacks.keys():
                    # stacks[char] = stacks[char].append(row[cur_key])
                    stacks[char].append(cur_box)
                    # ic(stacks)
                else:
                    stacks[char] = [cur_box]
                    # ic(stacks)
            # ic(stacks)
    # ic(key)
    return stacks, instructions


def part_one(stacks, instructions):

    for instruction in instructions:
        # ic("starting: ", stacks)
        # ic(instruction)
        _, num_boxes_to_move, _, from_stack, _, to_stack = instruction.split(' ')
        num_boxes_to_move = int(num_boxes_to_move)
        # ic(num_boxes_to_move, from_stack, to_stack)
        # # print(f"moving {num_boxes_to_move=} from {from_stack=} {stacks[from_stack]=} to {to_stack=} {stacks[to_stack]=}")
        # ic(stacks[to_stack])
        # ic(stacks[from_stack])

        for count in range(num_boxes_to_move):
            stacks[to_stack].append( stacks[from_stack].pop() )

        # below is a little less readable
        [stacks[to_stack].append(stacks[from_stack].pop()) for count in range(num_boxes_to_move)]


    message = ""
    # ic(stacks.items())
    for key, value in stacks.items():
        # ic(key)
        # ic(value)
        message += value.pop()
    ic(message)

    return


def part_two(stacks, instructions):

    for instruction in instructions:
        # ic("starting: ", stacks)
        # ic(instruction)
        _, num_boxes_to_move, _, from_stack, _, to_stack = instruction.split(' ')
        num_boxes_to_move = int(num_boxes_to_move)
        # ic(stacks)
        # ic(num_boxes_to_move, from_stack, to_stack)
        # # print(f"moving {num_boxes_to_move=} from {from_stack=} {stacks[from_stack]=} to {to_stack=} {stacks[to_stack]=}")
        # ic(stacks[to_stack])
        # ic(stacks[from_stack])

        # add X items to end of to_stack
        [stacks[to_stack].append(x) for x in stacks[from_stack][-num_boxes_to_move:]]

        # remove X items from end of from_stack
        stacks[from_stack] = stacks[from_stack][:-num_boxes_to_move]

    second_message = ""
    # ic(stacks.items())
    for key, value in stacks.items():
        # ic(key)
        # ic(value)
        second_message += value.pop()
    ic(second_message)

    return


@click.command()
@click.argument('file')
def main(file):
    data = data_array(file)
    # ic(data)

    stacks, instructions = parse_data_lines(data)
    part_one(stacks, instructions)

    # TODO: don't much with "stacks" everywhere
    stacks, instructions = parse_data_lines(data)
    part_two(stacks, instructions)
    
    ic()

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