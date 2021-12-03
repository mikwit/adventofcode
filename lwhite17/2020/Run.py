import argparse
import AoC_tools as AT


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", "-d", type=str, help="day's code to run")
    parser.add_argument("--part", "-p", type=str, default='b', help="which part to run (1 or 2 or both)")
    parser.add_argument("--input", "-i", type=str, help="path to input data file")
    parser.add_argument("-separator", '-s', type=str, default='\n', help="input data separator")

    args = parser.parse_args()

    data = AT.load_txt(args.input, sep=args.separator)

    ones = [1, "1", "one", "ONE", "One", "un", "UN", "une", "Un"]
    twos = [2, "2", "two", "TWO", "Two", "deux", "DEUX", "Deux"]

    if args.day in [1, "1", "one", "ONE", "One", "un", "UN", "une", "Un"]:
        import days.Day1 as Day
    elif args.day in [2, "2", "two", "TWO", "Two", "deux", "DEUX", "Deux"]:
        import days.Day2 as Day
    elif args.day in [3, "3", "three", "THREE", "Three", "trois", "TROIS", "Trois"]:
        import days.Day3 as Day
    elif args.day in [4, "4", "four", "FOUR", "Four", "quatre", "QUATRE", "Quatre"]:
        import days.Day4 as Day
    elif args.day in [5, "5", "five", "FIVE", "five", "cinq", "CINQ", "Cinq"]:
        import days.Day5 as Day
    elif args.day in [6, "6", "six", "SIX", "Six"]:
        import days.Day6 as Day
    elif args.day in [7, "7", "seven", "SEVEN", "Seven", "sept", "SEPT", "Sept"]:
        import days.Day6 as Day

    if args.part in ones:
        Day.part_one(data)
    elif args.part in twos:
        Day.part_two(data)
    else:
        Day.both(data)
