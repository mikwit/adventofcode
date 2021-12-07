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
        results = list(map(int, results[0].split(",")))

    return results


def get_crab_distance_vector(data):
    # get row of crab starting points
    data = np.array(data).reshape(1, len(data))
    # best target position will be between min and max starting positions
    # get max starting position
    pos_max = max(data[0])

    # return array of each crab's distance to each possible target pos
    pos_array = np.repeat(data, pos_max, axis=0)
    target_pos = np.array(list(range(pos_max)))
    target_pos = target_pos.reshape(len(target_pos), 1)
    crab_distances = abs(pos_array - target_pos)
    return crab_distances


def part_one(data):
    # part one fuel costs are constant per step
    crab_distances = get_crab_distance_vector(data=data)
    fuel_costs = crab_distances.sum(axis=1)
    least_fuel_spent = min(fuel_costs)
    return least_fuel_spent


def part_two(data):
    # part two fuel costs are triangular numbers
    # T_n = 1 + 2 + 3 + .. .+ (n-1) + n = n(n+1)/2 = (n^2 + n)/2
    # n is the number of horizontal steps for a single crab
    crab_distances = get_crab_distance_vector(data=data)
    fuel_costs = ((np.square(crab_distances) + crab_distances)/2).sum(axis=1)
    least_fuel_spent = min(fuel_costs)
    return least_fuel_spent


def both(data):
    print("Least (constant) fuel spent to align to best position: " + str(part_one(data)))
    print("Least (triangular) fuel spent to align to best position: " + str(part_two(data)))


if __name__ == '__main__':
    if input("Use pre-loaded data?\n") in ['y', 'Y', 'yes', 'Yes', 'YES']:
        use_data = load_txt('Data.txt', convert_to_type='int')
    else:
        use_data = load_txt(input("please enter data path: \n"), convert_to_type='int')
    # use_data = load_txt('SampleData.txt', convert_to_type='int')
    both(data=use_data)
