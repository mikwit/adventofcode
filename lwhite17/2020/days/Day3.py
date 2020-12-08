import AoC_tools as AT
import collections as col


slopeVar = col.namedtuple('slope', 'right, down')


def count_trees(course, slope):
    trees = 0
    column = 0
    width = len(course[0])

    for rInd, row in enumerate(course):
        # check descent
        if rInd % slope.down != 0:
            continue
        # get char
        char = row[column % width]
        if char == '#':
            trees += 1
        # move right
        column += slope.right
    return trees


def count_trees_third(course):
    m = slopeVar(3, 1)
    trees = count_trees(course=course, slope=m)
    return trees


def count_trees_slopes(course):
    prod = 1
    slopes = [slopeVar(1, 1), slopeVar(3, 1), slopeVar(5, 1), slopeVar(7, 1), slopeVar(1, 2)]

    # check each slope
    for slope in slopes:
        newTrees = count_trees(course, slope)
        prod *= newTrees

    return prod


def part_one(input_data):
    res = count_trees_third(input_data)
    print("\nnumber of trees: ", res)


def part_two(input_data):
    res = count_trees_slopes(input_data)
    print('\nproduct: ', res)


def both(input_data):
    res = count_trees_third(input_data)
    print("\nnumber of trees: ", res)
    res = count_trees_slopes(input_data)
    print('product: ', res)


if __name__ == '__main__':
    course = AT.load_txt(input("please enter data path: \n"))

    res = count_trees_third(course)
    print("\nnumber of trees: ", res)
    res = count_trees_slopes(course)
    print('product: ', res)
