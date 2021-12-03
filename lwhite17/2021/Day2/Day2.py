from collections import namedtuple


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


def find_planned_course(data):
    current_pos = namedtuple('Point', 'pos, depth')
    current_pos.pos = 0
    current_pos.depth = 0
    for entry in data:
        if 'forward' in entry:
            # forward increases horizontal position
            current_pos.pos += int(entry.strip()[-1:])
        elif 'up' in entry:
            # up decreases depth
            current_pos.depth -= int(entry.strip()[-1:])
        elif 'down' in entry:
            # down increases depth
            current_pos.depth += int(entry.strip()[-1:])
    return current_pos


def part_one(data):
    current_pos = find_planned_course(data=data)
    product = current_pos.pos * current_pos.depth
    return product


def find_manual_course(data):
    current_pos = namedtuple('Point', 'pos, aim, depth')
    current_pos.pos = 0
    current_pos.aim = 0
    current_pos.depth = 0
    for entry in data:
        if 'forward' in entry:
            # forward increases horizontal position
            value = int(entry.strip()[-1:])
            current_pos.pos += value
            current_pos.depth += current_pos.aim * value
        elif 'up' in entry:
            # up decreases depth
            current_pos.aim -= int(entry.strip()[-1:])
        elif 'down' in entry:
            # down increases depth
            current_pos.aim += int(entry.strip()[-1:])
    return current_pos


def part_two(data):
    current_pos = find_manual_course(data=data)
    return current_pos.depth * current_pos.pos


def both(data):
    print("Product of planned course's depth and location is: " + str(part_one(data)))
    print("Product of manual course's depth and location is: " + str(part_two(data)))


if __name__ == '__main__':
    if input("Use pre-loaded data?\n") in ['y', 'Y', 'yes', 'Yes', 'YES']:
        use_data = load_txt('Data.txt')
    else:
        use_data = load_txt(input("please enter data path: \n"))
    # use_data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    both(data=use_data)
