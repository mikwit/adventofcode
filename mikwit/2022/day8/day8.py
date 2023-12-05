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
    ic(content)
    return content


def part_one_previous(line):

    # for line in data:
    #     for char in line:
    #         ic(char)
    #         if line.index(char) > 2:
    #             cur_index = line.index(char)
    #             if len(set(line[cur_index - 3:cur_index + 1])) == 4:
    #                 ic(set(line[cur_index - 3:cur_index + 1]))
    #                 ic(cur_index)
    #                 return
    #             # else:
    #                 # ic(cur_index)

    cur_index = 0

    for char in line:
        # ic(char)
        # if line.index(char) > 2:
        if cur_index > 3:
            # cur_index = line.index(char)
            if len(set(line[cur_index - 3:cur_index + 1])) == 4:
                # ic(set(line[cur_index - 3:cur_index + 1]))
                # ic(cur_index + 1)
                print(f"{cur_index + 1=}")
                return
            # elif len(set(line[cur_index - 14:cur_index])) == 14:
                # print(f"{uhhhh}")
            else:
                cur_index += 1
        else:
            cur_index += 1
            # else:
                # ic(cur_index)


    return




def part_two_previous(line):

    # for line in data:
    #     for char in line:
    #         ic(char)
    #         if line.index(char) > 2:
    #             cur_index = line.index(char)
    #             if len(set(line[cur_index - 3:cur_index + 1])) == 4:
    #                 ic(set(line[cur_index - 3:cur_index + 1]))
    #                 ic(cur_index)
    #                 return
    #             # else:
    #                 # ic(cur_index)

    cur_index_two = 0

    for char in line:
        # ic(char)
        # if line.index(char) > 2:
        if cur_index_two > 13:
            # cur_index = line.index(char)
            if len(set(line[cur_index_two - 13:cur_index_two + 1])) == 14:
                # ic(set(line[cur_index - 3:cur_index + 1]))
                # ic(cur_index + 1)
                print(f"{cur_index_two + 1=}")
                return
            # elif len(set(line[cur_index - 14:cur_index])) == 14:
                # print(f"{uhhhh}")
            else:
                cur_index_two += 1
        else:
            cur_index_two += 1
            # else:
                # ic(cur_index)


    return


def get_columns(data):
    columns = ["" for char in data[0]] 
    for line in data:
        for index in range(len(line)):
            # ic(index)
            # if line.index(char) 
            columns[index] += line[index]
    return columns


def part_one(data):
    """
    shortest tree = 0
    largest tree = 9
    each number is a tree
    edge is:
        first digit in each line
        last digit in each line
        first line : if data.index(line) == 0
        last line : if data.index(line) + 1 == len(data)"""
    tree_map = data.copy()
    # tree_map.pop()
    ic(tree_map, data)

    """
    How many trees are visible from outside the grid?
    edge + some interior
    """

    # len(data) is the number of rows, is the number of trees on the left side
    # len(data[0]) is the number of columns, is th enumber of trees on the top
    # perimeter of rectangle = 2 ( l + w )
    # don't double count corners
    num_of_trees_on_edge = 2 * (len(data) - 1 + len(data[0]) - 1)
    ic(num_of_trees_on_edge)

    columns = get_columns(data)
    rows = [row for row in data]
    ic(columns, rows)

    inside_visible = 0
    cur_visible = 0

    # for row in rows:
    #     """30373"""
    #     for char in row:

    rows_from_left = rows.copy()
    rows_from_right = rows.copy()

    columns_from_top = columns.copy()
    columns_from_bottom = columns.copy()

    for row_index in range(len(rows_from_left)):
        row = rows_from_left[row_index]
        "30373"
        new_row = ""
        cur_max = row[0]

        for char_index in range(len(row)):
            cur_char = row[char_index]
            if char_index == 0:
                new_row += cur_char
                continue
            # if char_index == len(row) - 1:
            #     new_row += cur_char
            #     continue

            # if cur_char is greater than every char left of it, add it to row
            # else, add "0" to row
            # new_row += "0"

            # for left_chars in data[row_index][:column_index]:
            for left_chars in row[:char_index]:
                if int(left_chars) > int(cur_max):
                    cur_max = left_chars

            if cur_char > cur_max:
                new_row += cur_char
                # continue
            else:
                new_row += "0"

        ic(row, new_row)
    exit()


    # for row_index in range(len(rows)):
    #     row = rows[row_index]
    #     for char_index in range(len(row)):
    #         char = row[char_index]
    #         ic(row, char_index)
    #         [print("yes") for each_char in row if each_char >= char]


        # if row_index == 0:
        #     continue
        # if row_index == len(data) - 1:
        #     continue




    # for line in data:
    # for row_index in range(len(data)):
        
    #     if row_index == 0 or row_index == len(data) - 1:
    #         continue
        
    #     line = data[row_index]
        
    #     for column_index in range(len(line)):
        
    #         if column_index == 0 or column_index == len(line) - 1:
    #             continue
        
    #         char = line[column_index]
    #         ic(char, (column_index, row_index))

    #         """
    #         For my current char and indexes,
    #             if all chars left are smaller, inside_visible += 1
    #             elif all chars right are smaller, inside_visible += 1
    #             elif all column chars left are smaller, inside_visible += 1
    #             elif all column chars right are smaller, inside_visible += 1
    #         """



            
    #         # left_visible = "no"
    #         # # ic(line)
    #         # for left_char in data[row_index][:column_index]:
    #         #     # ic(data[row_index])
    #         #     # ic( data[row_index][:column_index] )
    #         #     if left_char >= char:
    #         #         left_visible = "no"
    #         #     else:
    #         #         left_visible = "yes"
    #         # ic(char, left_visible)
    #         # if left_visible == "yes":
    #         #     cur_visible += 1
    #         #     continue

    #         # # if i've gotten here, the current number is not left visible
    #         # right_visible = "no"
    #         # for right_char in data[row_index][column_index:]:
    #         #     ic(data[row_index][column_index+1:])
    #         #     if right_char >= char:
    #         #         right_visible = "no"
    #         #     else:
    #         #         right_visible = "yes"
    #         # ic(char, right_visible)
    #         # if right_visible == "yes":
    #         #     cur_visible += 1
    #         #     continue 

    ic(cur_visible)

            # if 
        # for char in line:
            # ic(char)

    # for 

    exit()
    return



@click.command()
@click.argument('file')
def main(file):
    data = data_array(file)
    # ic(data)

    part_one(data)

    exit()

    for line in data:
        part_one(line)
    # part_one(data)
    for line in data:
        part_two(line)

    exit()

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