import argparse


def load_txt(filename, sep=None, ignore_empties=True, convert_to_type=None):
    if sep is None:
        sep = '\n'
    with open(filename, 'r') as f:
        results = f.read().split(sep)

    if ignore_empties:
        for element in results:
            if len(element) == 0:
                results.remove(element)

    if convert_to_type == 'int':
        for ind, element in enumerate(results):
            results[ind] = int(element)

    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", "-f", type=str, help="path to data file", default='default')
    parser.add_argument("--day", "-d", type=str, help="day's code to run")
    parser.add_argument("--part", "-p", type=str, default='b', help="which part to run (1 or 2 or both)")
    parser.add_argument("--input", "-i", type=str, help="path to input data file")
    parser.add_argument("--datatype", "-dt", type=str, default='string', help='input data type')
    parser.add_argument("-separator", '-s', type=str, default='\n', help="input data separator")

    args = parser.parse_args()
    datatype = args.datatype

    ones = [1, "1", "one", "ONE", "One", "un", "UN", "une", "Un"]
    twos = [2, "2", "two", "TWO", "Two", "deux", "DEUX", "Deux"]

    if args.day in [1, "1", "one", "ONE", "One", "un", "UN", "une", "Un"]:
        import Day1.Day1 as Day
        if 'default' in args.filepath:
            filepath = 'Day1\Data.txt'
        if 'int' not in datatype:
            datatype = 'int'
    elif args.day in [2, "2", "two", "TWO", "Two", "deux", "DEUX", "Deux"]:
        import Day2.Day2 as Day
        if 'default' in args.filepath:
            filepath = 'Day2\Data.txt'
    elif args.day in [3, "3", "three", "THREE", "Three", "trois", "TROIS", "Trois"]:
        import Day3.Day3 as Day
        if 'default' in args.filepath:
            filepath = 'Day3\Data.txt'
    # elif args.day in [4, "4", "four", "FOUR", "Four", "quatre", "QUATRE", "Quatre"]:
    #     import Day4.Day4 as Day
    #     if 'default' in args.filepath:
    #         filepath = 'Day4\Data.txt'
    # elif args.day in [5, "5", "five", "FIVE", "five", "cinq", "CINQ", "Cinq"]:
    #     import Day5.Day5 as Day
    #     if 'default' in args.filepath:
    #         filepath = 'Day5\Data.txt'
    # elif args.day in [6, "6", "six", "SIX", "Six"]:
    #     import Day6.Day6 as Day
    #     if 'default' in args.filepath:
    #         filepath = 'Day6\Data.txt'
    # elif args.day in [7, "7", "seven", "SEVEN", "Seven", "sept", "SEPT", "Sept"]:
    #     import Day7.Day7 as Day
    #     if 'default' in args.filepath:
    #         filepath = 'Day7\Data.txt'
    # elif args.day in [8, "8", "eight", "EIGHT", "Eight", "huit", "HUIT", "Huit"]:
    #     import Day8.Day8 as Day
    #     if 'default' in args.filepath:
    #         filepath = 'Day8\Data.txt'
    # elif args.day in [9, "9", "nine", "NINE", "Nine", "neuf", "NEUF", "Neuf"]:
    #     import Day9.Day9 as Day
    #     if 'default' in args.filepath:
    #         filepath = 'Day9\Data.txt'
    #     if datatype in 'string':
    #         datatype = 'int'
    # elif args.day in [10, "10", "ten", "TEN", "Ten", "dix", "DIX", "Dix"]:
    #     import Day10.Day10 as Day
    #     if 'default' in args.filepath:
    #         filepath = 'Day19\Data.txt'
    #     if datatype in 'string':
    #         datatype = 'int'
    # elif args.day in [11, "11", "eleven", "ELEVEN", "Eleven", "onze", "ONZE", "Onze"]:
    #     import Day11.Day11 as Day
    #     if 'default' in args.filepath:
    #         filepath = 'Day11\Data.txt'

    # if not args.filepath:
    #     filepath = input("please enter data filepath:\n")
    # else:
    #     filepath = args.filepath

    if 'default' not in args.filepath:
        filepath = args.filepath

    data = load_txt(filepath, sep=args.separator, convert_to_type=datatype)

    if args.part in ones:
        Day.part_one(data)
    elif args.part in twos:
        Day.part_two(data)
    else:
        Day.both(data)
