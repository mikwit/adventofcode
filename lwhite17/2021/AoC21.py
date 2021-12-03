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
        import Days.Day1 as Day
    elif args.day in [2, "2", "two", "TWO", "Two", "deux", "DEUX", "Deux"]:
        import Days.Day2 as Day
    elif args.day in [3, "3", "three", "THREE", "Three", "trois", "TROIS", "Trois"]:
        import Days.Day3 as Day
    elif args.day in [4, "4", "four", "FOUR", "Four", "quatre", "QUATRE", "Quatre"]:
        import Days.Day4 as Day
    elif args.day in [5, "5", "five", "FIVE", "five", "cinq", "CINQ", "Cinq"]:
        import Days.Day5 as Day
    elif args.day in [6, "6", "six", "SIX", "Six"]:
        import Days.Day6 as Day
    elif args.day in [7, "7", "seven", "SEVEN", "Seven", "sept", "SEPT", "Sept"]:
        import Days.Day7 as Day
    elif args.day in [8, "8", "eight", "EIGHT", "Eight", "huit", "HUIT", "Huit"]:
        import Days.Day8 as Day
    elif args.day in [9, "9", "nine", "NINE", "Nine", "neuf", "NEUF", "Neuf"]:
        import Days.Day9 as Day
        if datatype in 'string':
            datatype = 'int'
    elif args.day in [10, "10", "ten", "TEN", "Ten", "dix", "DIX", "Dix"]:
        import Days.Day10 as Day
        if datatype in 'string':
            datatype = 'int'
    elif args.day in [11, "11", "eleven", "ELEVEN", "Eleven", "onze", "ONZE", "Onze"]:
        import Days.Day11 as Day

    data = load_txt(args.input, sep=args.separator, convert_to_type=datatype)

    if args.part in ones:
        Day.part_one(data)
    elif args.part in twos:
        Day.part_two(data)
    else:
        Day.both(data)
