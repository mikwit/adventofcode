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


# def simulate_lanternfish(data, days):
#     for day in range(days):
#         data = np.append(data, 9*np.ones(len(data[data == 0])))
#         data[data == 0] = 7
#         data[data > 0] -= 1
#     return data


def model_lanternfish(data, days):
    phase = np.zeros(9)
    start_population = np.bincount(np.array(data))
    phase[:len(start_population)] = start_population

    for day in range(days):
        no_babies = phase[0]
        phase[:8] = phase[1:]
        phase[6] += no_babies
        phase[8] = no_babies

    population = phase.sum()
    return population


def part_one(data, days=80):
    # population = simulate_lanternfish(data=data, days=days)
    population = model_lanternfish(data=data, days=days)
    return population


def part_two(data, days=256):
    # population = simulate_lanternfish(data=data, days=days)
    population = model_lanternfish(data=data, days=days)
    return population


def both(data):
    data = np.array(list(map(int, data[0].split(","))))
    print("Number of lanternfish alive after 80 days: " +
          str(part_one(data=data, days=80)))
    print("Number of lanternfish alive after 256 days: " +
          str(part_two(data=data, days=256)))


if __name__ == '__main__':
    if input("Use pre-loaded data?\n") in ['y', 'Y', 'yes', 'Yes', 'YES']:
        use_data = load_txt('Data.txt')
    else:
        use_data = load_txt(input("please enter data path: \n"))
    # use_data = load_txt('SampleData.txt')
    both(data=use_data)
