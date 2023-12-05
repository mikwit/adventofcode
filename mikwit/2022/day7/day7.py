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

    # return final_dict


# class Dir:
#     """A dir cannot have a direct size; only files have sizes"""
#     def __init__(self, name):
#         self.name = name
    

# class File:
#     def __init__(self, name, size, ):
#         self.name = name
#         self.size = size
"""
{
    /:
        a:
            ""
        b.txt: 14848514
        c.dat: 8504156
        d:
            ""
}
"""


# class Tree:
#     def __init__(self):
#         self.left = None
#         self.right = None
#         self.data = None


# class TreeNode():
#     def __init__(self, value):
#         self.value = value # data
#         self.children = [] # references to other nodes
    
#     def add_child(self, child_node):
#         # creates parent-child relationship
#         print(f"Adding {child_node.value}")
#         self.children.append(child_node)

#     def remove_child(self, child_node):
#         # removes parent-child relationship
#         print(f"Removing {child_node.value} from {self.value}")
#         self.children = [child for child in self.children if child is not child_node]
    
#     def traverse(self):
#         # moves through each node referenced from self downwards
#         nodes_to_visit = [self]
#         while len(nodes_to_visit) > 0:
#             current_node = nodes_to_visit.pop()
#             print(current_node.value)
#             nodes_to_visit += current_node.children


def parse(input):
    output = ""
    if input.startswith("$ cd "):
        # _, output = input.split("$ cd ")
        # return output
        """return _, cdtarget"""
        return input.split("$ cd ")
    elif input.startswith("dir "):
        # _, output = input.split("dir ")
        """return _, dirname"""
        return input.split("dir ")
    else:
        """return size, filename"""
        return input.split(" ")


def part_one(data):

    """
    For any directories with a total size of 100,000 and less,
    add them all up and report combined size
    """

    from collections import defaultdict
    filestructure = defaultdict(int)
    path = []
    for line in data:
        # ic(path)
        words = line.strip().split()
        if words[1] == "cd":
            if words[2] == "..":
                path.pop()
            else:
                path.append(words[2])
        elif words[1] == 'ls':
            continue
        elif words[0] == 'dir':
            continue
        else:
            # ic(path, words)
            # ic(path, words[0])
            filesize = int(words[0])
            # ic(filesize)
            # ic(filesize, path, len(path))
            num_of_dirs = range(len(path) + 1)
            for dir_num in num_of_dirs:
                # add filesize to every dir in current path
                filestructure['/'.join(path[:dir_num])] += filesize
                # ic(filestructure)
            # ic(words[1])
    ic(filestructure)
    total_size_of_dirs_under_100k = 0
    for each_dir, value in filestructure.items():
        if value <= 100000:
            total_size_of_dirs_under_100k += value
    ic(total_size_of_dirs_under_100k)

    space_needed = 30000000
    total_space = 70000000
    current_used_space = filestructure['/']
    # ic(current_used_space)
    unused_space = total_space - current_used_space
    # ic(unused_space)

    space_to_free_up = space_needed - unused_space
    # ic(space_to_free_up)

    total_size_of_dir_to_delete = total_space
    dir_to_delete = ""
    for each_dir, value in filestructure.items():
        if value >= space_to_free_up:
            if value <= total_size_of_dir_to_delete:
                total_size_of_dir_to_delete = value
                dir_to_delete = each_dir
    # ic(total_size_of_dir_to_delete, dir_to_delete)
    ic(total_size_of_dir_to_delete)
    


    return




def part_two(line):

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