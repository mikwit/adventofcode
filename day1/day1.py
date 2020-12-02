import sys
# import argparse

# parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
# parser.add_argument(i'file', '--file'. help='please give me a file to read from')
# args = parser.parse_args()


def data_array(input_file="data.txt"):
    in_file = open(input_file, "r")
    with open(input_file) as f:
        content = f.read().strip()
        array_of_input = content.split()
        final_array = [int(each_int) for each_int in array_of_input]
    return final_array


def find_2020_pairs(expenses):
    pairs_dict = {}

    for expense in expenses:
        for other_expense in expenses:
            exp_total = expense + other_expense
            if (exp_total == 2020):
                product = expense * other_expense
                if product not in pairs_dict.keys():
                    pairs_dict[product] = [expense, other_expense]
                    # print(f"pairs_dict: {pairs_dict}")

    keys = pairs_dict.keys()
    if not keys:
        sys.exit("ERROR: no pairs")
    return list(keys)


def find_2020_triples(expenses):
    triples_dict = {}

    for expense in expenses:
        for other_expense in expenses:
            for third_expense in expenses:
                exp_total = expense + other_expense + third_expense
                if (exp_total == 2020):
                    product = expense * other_expense * third_expense
                    if product not in triples_dict.keys():
                        triples_dict[product] = [expense, other_expense, third_expense]
                        # print(f"triples_dict: {triples_dict}")

    keys = triples_dict.keys()
    if not keys:
        sys.exit("ERROR: no triples")
    return list(keys)


def main():
    expenses = data_array()
    # test a subset
    # data = data[:5]
    # data.append(479)
    # print(f"expenses = {expenses}")

    pairs = find_2020_pairs(expenses)
    print(f"products for 2 expenses that sum to 2020: {pairs}")

    triples = find_2020_triples(expenses)
    print(f"products for 3 expenses that sum to 2020: {triples}")

    return


if __name__ == "__main__":

    # parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
    # parser.add_argument('--file', '-f', dest='file', help='please give me a file to read from')
    # parser.add_argument('--verbose', '-v', action='count', help='let me know if you want to see more details')
    # args = parser.parse_args()
    # print(dup_finder(args.file, args.verbose, 0))
    # print(file_duplicator(args.file, args.verbose, 0))

    main()