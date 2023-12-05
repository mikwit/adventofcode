import numpy as np


def load_txt(filename, sep=None, ignore_empties=True, convert_to_type=None):
    if sep is None:
        sep = '\n'
    with open(r'' + filename, 'r') as f:
        results = f.read().split(sep)
    if ignore_empties:
        for element in results:
            if len(element) == 0:
                results.remove(element)
    if convert_to_type == 'int':
        for ind, element in enumerate(results):
            results[ind] = int(element)

    return results


def format_data(data):
    lines = []
    for line in data:
        # create four-element list of vent (line) ends
        line = line.split()
        start = list(map(int, line[0].split(",")))
        end = list(map(int, line[2].split(",")))
        full_line = start + end
        # add to list of vents (lines)
        lines.append(full_line)

    max_dimension = max(max(lines)) + 5
    return lines, max_dimension


def map_floor(floor, lines, diagonal):
    for vent in lines:
        # verticle line
        if vent[0] == vent[2]:
            start = min(vent[1], vent[3])
            end = max(vent[1], vent[3]) + 1
            floor[start:end, vent[0]] += 1

        # horizontal line
        elif vent[1] == vent[3]:
            start = min(vent[0], vent[2])
            end = max(vent[0], vent[2]) + 1
            floor[vent[1], start:end] += 1

        # diagonal line
        elif diagonal:
            # slope is up due to y
            if vent[1] > vent[3]:
                row_range = np.array(np.arange(vent[1], vent[3] - 1, -1))
            # slope is down due to y
            else:
                row_range = np.array(np.arange(vent[1], vent[3] + 1))
            # slope is up due to x
            if vent[0] > vent[2]:
                col_range = np.array(np.arange(vent[0], vent[2] - 1, -1))
            # slope is down due to x
            else:
                col_range = np.array(np.arange(vent[0], vent[2] + 1))
            floor[row_range, col_range] += 1

    return floor


def part_one(lines, max_dimension):
    floor = np.zeros((max_dimension, max_dimension))
    floor = map_floor(floor=floor, lines=lines, diagonal=False)
    # count points of intersection
    count = len(floor[floor > 1])
    return count


def part_two(lines, max_dimension):
    floor = np.zeros((max_dimension, max_dimension))
    floor = map_floor(floor=floor, lines=lines, diagonal=True)
    # count points of intersection
    count = len(floor[floor > 1])
    return count


def both(data):
    lines, max_dimension = format_data(data=data)
    print("Number of overlapping orthogonal vent points: " + str(part_one(lines=lines, max_dimension=max_dimension)))
    print("Number of overlapping vent points: " + str(part_two(lines=lines, max_dimension=max_dimension)))


if __name__ == '__main__':
    if input("Use pre-loaded data?\n") in ['y', 'Y', 'yes', 'Yes', 'YES']:
        use_data = load_txt('Data.txt')
    else:
        use_data = load_txt(input("please enter data path: \n"))
    both(data=use_data)
