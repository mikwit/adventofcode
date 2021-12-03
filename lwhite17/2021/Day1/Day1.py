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


def count_inc_depth(data):
    increments = 0
    prev_entry = None
    for entry in data:
        if not prev_entry:
            pass
        elif entry > prev_entry:
            increments += 1
        prev_entry = entry
    return increments


def count_inc_sums(data):
    increments = 0
    prev_sum = None
    for ind in range(len(data)):
        subset = data[ind-2:ind+1]
        if len(subset) != 3:
            continue
        current_sum = sum(subset)
        if not prev_sum:
            pass
        else:
            if current_sum > prev_sum:
                increments += 1
        prev_sum = current_sum
    return increments


def part_one(data):
    return count_inc_depth(data=data)


def part_two(data):
    return count_inc_sums(data=data)


def both(data):
    print('number of increments in single measurements: ' +
          str(count_inc_depth(data=data)))
    print('number of increments in sums of measurements: ' +
          str(count_inc_sums(data=data)))


if __name__ == '__main__':
    if input("Use pre-loaded data?\n") in ['y', 'Y', 'yes', 'Yes', 'YES']:
        use_data = load_txt('Data.txt', convert_to_type='int')
    else:
        use_data = load_txt(input("please enter data path: \n"))
    both(data=use_data)
