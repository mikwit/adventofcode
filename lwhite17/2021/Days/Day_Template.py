# imports


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


def part_one(data):
    return 0


def part_two(data):
    return 0


def both(data):
    return 0


if __name__ == '__main__':
    if input("Use pre-loaded data?\n") in ['y', 'Y', 'yes', 'Yes', 'YES']:
        use_data = load_txt(r'C:\Users\leaht\Documents\AoC\2021\Data\Data_Day_.txt')
    else:
        use_data = load_txt(input("please enter data path: \n"))
    both(data=use_data)
