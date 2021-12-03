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
    data_list = []
    for entry in data:
        entry_list = [int(val) for val in entry]
        data_list.append(entry_list)

    data_array = np.array(data_list)
    return data_array


def run_diagnostic_report(data):
    gamma_rate_str = [str(np.bincount(data[:, i]).argmax()) for i in range(data.shape[1])]
    gamma_rate_str = "".join(gamma_rate_str)
    gamma_rate_val = int(gamma_rate_str, 2)

    epsilon_rate_str = [str(np.bincount(data[:, i]).argmin()) for i in range(data.shape[1])]
    epsilon_rate_str = "".join(epsilon_rate_str)
    epsilon_rate_val = int(epsilon_rate_str, 2)
    return gamma_rate_val, epsilon_rate_val


def part_one(data):
    gamma, epsilon = run_diagnostic_report(data=data)
    return gamma * epsilon


def find_rating_value(data, criteria):
    remaining_data = data
    # sift through data to eliminate rating values
    for i in range(data.shape[1]):
        # count number of 0's and 1's
        counts = np.bincount(remaining_data[:, i])
        # use most common values for oxygen
        if 'max' in criteria:
            if counts[0] == counts[1]:
                crit_val = 1
            else:
                crit_val = counts.argmax(axis=0)
        # use least common values for carbon
        else:
            if counts[0] == counts[1]:
                crit_val = 0
            else:
                crit_val = counts.argmin(axis=0)
        remaining_data = remaining_data[remaining_data[:, i] == int(crit_val)]
        if remaining_data.shape[0] == 2:
            if 'max' in criteria:
                remaining_data = remaining_data[remaining_data[:, i+1] == 1]
            else:
                remaining_data = remaining_data[remaining_data[:, i+1] == 0]
            break
        if remaining_data.shape[0] == 1:
            break

    # get first row of multidimensional array
    rating_array = remaining_data[0]
    # convert array to a list of string integers to a string binary number
    rating_str = "".join([str(val) for val in rating_array])
    # convert binary to decimal
    rating_val = int(rating_str, 2)
    return rating_val


def run_life_support_rating(data):
    oxygen_rating = find_rating_value(data=data, criteria='max')
    carbon_rating = find_rating_value(data=data, criteria='min')
    return oxygen_rating, carbon_rating


def part_two(data):
    oxygen_rating, carbon_rating = run_life_support_rating(data=data)
    return oxygen_rating * carbon_rating


def both(data):
    print('Power consumption of submarine is: ' + str(part_one(data=data)))
    print('Life support rating of submarine is: ' + str(part_two(data=data)))


if __name__ == '__main__':
    if input("Use pre-loaded data?\n") in ['y', 'Y', 'yes', 'Yes', 'YES']:
        use_data = load_txt(r'C:\Users\leaht\Documents\AoC\2021\Data\Data_Day_3.txt')
    else:
        use_data = load_txt(input("please enter data path: \n"))

    # example data
    # use_data = ['00100', '11110', '10110', '10111', '10101', '01111',
    #             '00111', '11100', '10000', '11001', '00010', '01010']

    use_data = format_data(data=use_data)
    both(data=use_data)
