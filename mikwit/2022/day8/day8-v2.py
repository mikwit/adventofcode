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


def other_part_one(data):
    from collections import defaultdict
    ans = 0

    G = []
    for line in data:
        row = line
        G.append(row)
    # G = []

    DIR = [(-1,0),(0,1),(1,0),(0,-1)]
    R = len(G)
    C = len(G[0])

    for r in range(R):
        for c in range(C):
            vis = False
            rr = r
            cc = c
            for (dr,dc) in DIR:
                ok = True
                while True:
                    rr += dr
                    cc += dc
                    if not (0<=rr<R and 0<=cc<C):
                        break
                    if G[rr][cc] >= G[r][c]:
                        ok = False
                if ok:
                    vis = True
            if vis:
                ans += 1
    print(ans)
    return


def part_one(data):
    grid = [list(map(int, line)) for line in data]
    # ic(grid)

    trees_visible = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            cur_tree = grid[row][col]
            """
            if all of the trees to the left of the current tree are less than the current tree, where x is all of the column indeces less than cur_tree's index
            or if all of the trees to the right are shorter
            or if all of the ones above it are shorter
            or if all of the ones below it are shorter
            """
            if (
                all(grid[row][left_tree] < cur_tree for left_tree in range(col))
                or all(grid[row][right_tree] < cur_tree for right_tree in range(col + 1, len(grid[row])))
                or all(grid[above_tree][col] < cur_tree for above_tree in range(row))
                or all(grid[below_tree][col] < cur_tree for below_tree in range(row + 1, len(grid)))
            ):
                trees_visible += 1
    ic(trees_visible)

    return


def part_two(data):
    grid = [list(map(int, line)) for line in data]
    # ic(grid)

    highest_scenic_score = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            cur_tree = grid[row][col]

            L = R = U = D = 0

            for x in range(col - 1, -1, -1):
                L += 1
                # if our tree is same height
                if grid[row][x] >= cur_tree:
                    break
            for x in range(col + 1, len(grid[row])):
                R += 1
                if grid[row][x] >= cur_tree:
                    break
            for x in range(row - 1, -1, -1):
                U += 1
                if grid[x][col] >= cur_tree:
                    break
            for x in range(row + 1, len(grid)):
                D += 1
                if grid[x][col] >= cur_tree:
                    break
            highest_scenic_score = max(highest_scenic_score, L * R * U * D)


    ic(highest_scenic_score)

    return


@click.command()
@click.argument('file')
def main(file):
    data = data_array(file)
    # ic(data)

    part_one(data)

    part_two(data)

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