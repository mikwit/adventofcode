import sys

# import argparse

# parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
# parser.add_argument(i'file', '--file'. help='please give me a file to read from')
# args = parser.parse_args()

# 123456789012
# 000011110010

def data_array(input_file="data.txt"):
    with open(input_file) as f:
        content = f.read().strip()
        # print(f"{content}")
        array_of_input = content.split('\n')
        # print(f"{array_of_input}")

        # for line in content:
        # exit()
        # 
        # array_of_input = content.split()
        # final_array = [int(each_int) for each_int in array_of_input]
        # print(f"{final_array}")
        # exit()
    return array_of_input
    # return final_array


def get_gamma(data):

    gamma_array = []

    i = 0
    for bit in range(12):
        # print(f"char: {bit}")

        current_bit_array = []

        for line in data:
            # print(f"{line[i]}")
            current_bit_array.append(line[i])
        i += 1
        # print(f"current_bit_array: {current_bit_array}")

        # print(f"{current_bit_array.count('1')}")

        if current_bit_array.count("1") > current_bit_array.count("0"):
            gamma_array.append(1)
        elif current_bit_array.count("0") > current_bit_array.count("1"):
            gamma_array.append(0)
        else:
            print(f"!!! ERROR! SAME FREQUENCY")
    print(f"gamma array: {gamma_array}")

    gamma = ""
    for bit in gamma_array:
        gamma += str(bit)
    print(f"gamma: {gamma}")

    # print(f"done")
    return gamma

def get_epsilon(data):

    epsilon_array = []

    i = 0
    for bit in range(12):
        # print(f"char: {bit}")

        current_bit_array = []

        for line in data:
            # print(f"{line[i]}")
            current_bit_array.append(line[i])
        i += 1
        # print(f"current_bit_array: {current_bit_array}")

        # print(f"{current_bit_array.count('1')}")

        if current_bit_array.count("1") > current_bit_array.count("0"):
            epsilon_array.append(0)
        elif current_bit_array.count("0") > current_bit_array.count("1"):
            epsilon_array.append(1)
        else:
            print(f"!!! ERROR! SAME FREQUENCY")
    print(f"epsilon array: {epsilon_array}")

    epsilon = ""
    for bit in epsilon_array:
        epsilon += str(bit)

    # print(f"done")
    return epsilon


def get_most_common(list_of_values):
    # print(f"list_of_values: {list_of_values}")
    # if list_of_values.count("0") > list_of_values.count("1"):
    #     return 0
    # elif list_of_values.count("0") < list_of_values.count("1"):
    #     return 1
    # elif list_of_values.count(0) > list_of_values.count(1):
    #     return 0
    # elif list_of_values.count(0) < list_of_values.count(1):
    #     return 1
    # else:
    #     # print(f"!!! equal 1 and 0")
    #     return 1

    if list_of_values.count("0") > list_of_values.count("1"):
        return 0
    elif list_of_values.count("0") < list_of_values.count("1"):
        return 1
    elif list_of_values.count(0) > list_of_values.count(1):
        return 0
    elif list_of_values.count(0) < list_of_values.count(1):
        return 1
    else:
        return 1

    # return


def get_least_common(list_of_values):
    # print(f"list_of_values: {list_of_values}")
    if list_of_values.count("0") > list_of_values.count("1"):
        return 1
    elif list_of_values.count("0") < list_of_values.count("1"):
        return 0
    elif list_of_values.count(0) > list_of_values.count(1):
        return 1
    elif list_of_values.count(0) < list_of_values.count(1):
        return 0
    else:
        return 0
    # return


def get_all_pos_x_of_lines(lines, pos):
    pos_array = []
    for line in lines:
        pos_array.append(line[pos])
    return pos_array


def get_o2(data):
    # all_pos1 = get_all_pos_x_of_lines(data, 0)
    # pos1_common = get_common(all_pos1, 0, 1, 1)
    # print(f"pos1_common: {pos1_common}")

    # trimmed_data = []
    # for line in data:
    #     if line.startswith(pos1_common)
    #         trimmed_data.append(line)

    trimmed_data = []
    for line in data:
        # print(f"line: {line}")
        # exit()
        trimmed_data.append(line)
        # print(f"{trimmed_data}")
    # exit()
    for pos in range(12):
        if len(trimmed_data) == 1:
            print(f"trimmed_data done: {trimmed_data}")
            return trimmed_data[0]
        # print(f"pos {pos} in progress")
        # print(f"trimmed_data: {trimmed_data}")
        all_current_pos = get_all_pos_x_of_lines(trimmed_data, pos)
        current_pos_common = get_most_common(all_current_pos)
        # print(f"most common for {pos} is {current_pos_common}")
        temp_data = trimmed_data.copy()
        for line in temp_data:
            # print(f"asdf {line[pos]}")
            if int(line[pos]) != int(current_pos_common):
                # trimmed_data.pop(line)
                trimmed_data.remove(line)
                # while line in trimmed_data:
                    # trimmed_data.remove(line)
                # print(f"removed {line} because it did not have {current_pos_common} at pos {pos}")
    # print(f"trimmed_data: {trimmed_data}")
    # exit()

    if len(trimmed_data) == 1:
        print(f"trimmed_data: {trimmed_data}")
        return trimmed_data[0]
    else:
        print(f"crap")
        exit()
    # return 


def get_co2(data):

    trimmed_data = []
    for line in data:
        # print(f"line: {line}")
        # exit()
        trimmed_data.append(line)
        # print(f"{trimmed_data}")
    # exit()
    for pos in range(12):
        # print(f"trimmed_data: {trimmed_data}")
        if len(trimmed_data) == 1:
            return trimmed_data[0]
        # print(f"pos {pos} in progress")
        all_current_pos = get_all_pos_x_of_lines(trimmed_data, pos)
        current_pos_common = get_least_common(all_current_pos)
        # print(f"least common for {pos} is {current_pos_common}")
        temp_data = trimmed_data.copy()
        for line in temp_data:
            # print(f"asdf {line[pos]}")
            if int(line[pos]) != int(current_pos_common):
                # trimmed_data.pop(line)
                while line in trimmed_data:
                    trimmed_data.remove(line)
                # print(f"removed {line} because it did not have {current_pos_common} at pos {pos}")
    # print(f"trimmed_data: {trimmed_data}")
    # exit()

    if len(trimmed_data) == 1:
        return trimmed_data[0]
    else:
        print(f"crap")
        exit()
    # return 


# def get_o2(data):

#     o2_array = []

#     i = 0
#     for bit in range(12):
#         print(f"char: {bit}")

#         current_bit_array = []

#         for line in data:
#             # print(f"{line[i]}")
#             current_bit_array.append(line[i])
#         i += 1
#         # print(f"current_bit_array: {current_bit_array}")

#         print(f"{current_bit_array.count('1')}")

#         if current_bit_array.count("1") > current_bit_array.count("0"):
#             o2_array.append(1)
#         elif current_bit_array.count("0") > current_bit_array.count("1"):
#             o2_array.append(0)
#         else:
#             # print(f"!!! ERROR! SAME FREQUENCY")
#             o2_array.append(1)
#     print(f"o2_array: {o2_array}")

#     o2 = ""
#     for bit in o2_array:
#         o2 += str(bit)

#     # print(f"done")
#     return o2

def main():
    data = data_array()
    # test a subset
    # data = data[:5]
    # data.append(479)
    # print(f"expenses = {expenses}")

    # final_position = plot_course(data)
    # print(f"final position (horizontal * vertical) = {final_position}")

    # final_correct_pos = plot_corrected_course(data)
    # print(f"final correct position (horizontal * vertical) = {final_correct_pos}")

    gamma = int(get_gamma(data), 2)
    # exit()
    epsilon = int(get_epsilon(data), 2)
    print(f"{gamma}")
    print(f"{epsilon}")
    # exit()
    print(f"gamma, epsilon, multiplied: {gamma}, {epsilon}, {gamma * epsilon}")
    o2 = int(get_o2(data), 2)
    print(f"o2: {o2}")

    co2 = int(get_co2(data), 2)
    print(f"co2: {co2}")

    print(f"o2 * c02 = {o2 * co2}")
    # print(f"final position (horizontal * vertical) = {final_position}")


    return


if __name__ == "__main__":

    # parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
    # parser.add_argument('--file', '-f', dest='file', help='please give me a file to read from')
    # parser.add_argument('--verbose', '-v', action='count', help='let me know if you want to see more details')
    # args = parser.parse_args()
    # print(dup_finder(args.file, args.verbose, 0))
    # print(file_duplicator(args.file, args.verbose, 0))

    main()
