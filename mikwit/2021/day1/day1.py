import sys

# import argparse

# parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
# parser.add_argument(i'file', '--file'. help='please give me a file to read from')
# args = parser.parse_args()


def data_array(input_file="data.txt"):
    with open(input_file) as f:
        content = f.read().strip()
        array_of_input = content.split()
        final_array = [int(each_int) for each_int in array_of_input]
        # print(f"{final_array}")
    return final_array


# def find_2020_pairs(expenses):
#     pairs_dict = {}

#     for expense in expenses:
#         for other_expense in expenses:
#             exp_total = expense + other_expense
#             if exp_total == 2020:
#                 product = expense * other_expense
#                 if product not in pairs_dict.keys():
#                     pairs_dict[product] = [expense, other_expense]
#                     # print(f"pairs_dict: {pairs_dict}")

#     keys = pairs_dict.keys()
#     if not keys:
#         sys.exit("ERROR: no pairs")
#     return list(keys)


# def find_2020_triples(expenses):
#     triples_dict = {}

#     for expense in expenses:
#         for other_expense in expenses:
#             for third_expense in expenses:
#                 exp_total = expense + other_expense + third_expense
#                 if exp_total == 2020:
#                     product = expense * other_expense * third_expense
#                     if product not in triples_dict.keys():
#                         triples_dict[product] = [expense, other_expense, third_expense]
#                         # print(f"triples_dict: {triples_dict}")

#     keys = triples_dict.keys()
#     if not keys:
#         sys.exit("ERROR: no triples")
#     return list(keys)


def find_increased_count(data):
    length = len(data)
    print(f"there are {length} items in the list")
    counter = 0
    i = 1
    increase_decrease_list = ["N/A - no previous measurement"]
    for item in data[1:]:
        previous_item = data[i - 1]
        i += 1
        # previous_item = data[data.index(item) - 1]
        if item > previous_item:
            increase_decrease_list.append("increased")
            counter += 1
            print(f"increased, {item} > {previous_item}, total times is {counter}")
        elif item < previous_item:
            increase_decrease_list.append("decreased")
            print(f"decreased, {item} < {previous_item}")
        else:
            increase_decrease_list.append("no change")
            print(f"no change, {item} == {previous_item}")
    # print(f"{increase_decrease_list}")
    return increase_decrease_list.count("increased")


def increased_count_windows(data):
    i = 0
    counter = 0
    new_data_list = []
    length = len(data)
    # pad data with 2 extra numbers bc lazy
    # data.append(0)
    # data.append(0)
    for item in data:
        if i < (length - 2):
            new_data_point = data[i] + data[i + 1] + data[i + 2]
            new_data_list.append(new_data_point)
            i += 1
    print(f"{new_data_list}")
    # exit()

    new_data_list_count = find_increased_count(new_data_list)

    return new_data_list_count


def main():
    data = data_array()
    # test a subset
    # data = data[:5]
    # data.append(479)
    # print(f"expenses = {expenses}")

    number_increased = find_increased_count(data)
    print(f"increased count: {number_increased}")

    number_increased_windows = increased_count_windows(data)
    print(f"increased count windows: {number_increased_windows}")

    # pairs = find_2020_pairs(expenses)
    # print(f"products for 2 expenses that sum to 2020: {pairs}")

    # triples = find_2020_triples(expenses)
    # print(f"products for 3 expenses that sum to 2020: {triples}")

    return


if __name__ == "__main__":

    # parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
    # parser.add_argument('--file', '-f', dest='file', help='please give me a file to read from')
    # parser.add_argument('--verbose', '-v', action='count', help='let me know if you want to see more details')
    # args = parser.parse_args()
    # print(dup_finder(args.file, args.verbose, 0))
    # print(file_duplicator(args.file, args.verbose, 0))

    main()
