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


class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


class TreeNode():
    def __init__(self, value):
        self.value = value # data
        self.children = [] # references to other nodes
    
    def add_child(self, child_node):
        # creates parent-child relationship
        print(f"Adding {child_node.value}")
        self.children.append(child_node)

    def remove_child(self, child_node):
        # removes parent-child relationship
        print(f"Removing {child_node.value} from {self.value}")
        self.children = [child for child in self.children if child is not child_node]
    
    def traverse(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children


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

    # root = Tree()
    # root = TreeNode
    cur_parent = ""
    for line in data:
        ic(line)
        if line.startswith("$ ls"):
            """useless"""
            continue
        elif line.startswith("$ cd"):
            cd_target = parse(line)[1]
            if cd_target == "/": # target is root
            # if line == "$ cd /":
                print(f"{parse(line)=}")
                # exit()
                # root = TreeNode(parse(line)[1])
                root = TreeNode(cd_target)
                ic(root.value)
                # exit()
            elif cd_target == "..":
                # target is parent
                pass
            else: # target is a recently added child child
                # root.add_child(cd_target)
                # ic(root.children)
                pass
        elif line.startswith("dir "):
            # ic(parse(line)[1])
            root.add_child( TreeNode(parse(line)[1]) )
            ic([child.value for child in root.children])
        elif line[0].isdigit():
            root.add_child(line)
            ic([child.value for child in root.children])

            # if line == "$ cd ..":
                # continue
    # exit()
    zzz = {}

    structure = {}

    cur_directory = ""
    cur_dir = ""
    
    for line in data:
        ic(line)

        if line.startswith("$ ls"):
            continue
        elif line.startswith("$ cd"):
            if line == "$ cd ..":
                """change current dir to parent"""
                # cur_dir = structure[]
                continue
            else:
                """change current dir to dir in current dir"""
                _, cur_dir = parse(line)
        elif line.startswith("dir "):
            """empty dir should be added to current dir"""
            pass
        else:
            """size, file should be added to current dir"""
            pass


        if line.startswith("$ "):
            if line.startswith("$ cd .."):
                cur_directory = "?"
            elif line.startswith("$ cd"):
                if ".." in line:
                    ic()
                else:
                    _, cur_directory = line.split('$ cd ')
                    ic(cur_directory)
                    if not cur_directory in zzz:
                        zzz[cur_directory].append("")
        else:
            if line.startswith("dir "):
                ic()
            else:
                # zzz[cur_directory]
                pass
            

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

    # cur_index = 0

    # for char in line:
    #     # ic(char)
    #     # if line.index(char) > 2:
    #     if cur_index > 3:
    #         # cur_index = line.index(char)
    #         if len(set(line[cur_index - 3:cur_index + 1])) == 4:
    #             # ic(set(line[cur_index - 3:cur_index + 1]))
    #             # ic(cur_index + 1)
    #             print(f"{cur_index + 1=}")
    #             return
    #         # elif len(set(line[cur_index - 14:cur_index])) == 14:
    #             # print(f"{uhhhh}")
    #         else:
    #             cur_index += 1
    #     else:
    #         cur_index += 1
    #         # else:
    #             # ic(cur_index)


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