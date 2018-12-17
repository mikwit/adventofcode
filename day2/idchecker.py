import argparse

def char_counter(boxid="", verbosity=""):
    boxid = boxid
    seen = []
    seen_twice = []
    seen_thrice = []

    count_two = 0
    count_three = 0

    for b in boxid:
        if b not in seen:
            seen.append(b)
        else:
            if b not in seen_twice:
                seen_twice.append(b)
            else:
                if b not in seen_thrice:
                    seen_thrice.append(b)

    for item in seen_twice:
        if item not in seen_thrice:
            count_two = 1
        else:
            count_three = 1

    counts = [count_two, count_three]

    return(counts)


def id_checker(input_file="", verbosity=""):
    # in_file = open(input_file, "r")
    boxids = open(input_file).readlines()
    boxids = [x.strip() for x in boxids]

    if verbosity:
        print("boxids: {}".format(boxids))
        print("")

    boxids_with_two = 0
    boxids_with_three = 0
    for bid in boxids:
        if char_counter(bid, verbosity)[0] == 1:
            if verbosity:
                print("duplicate in {0}".format(bid))
            boxids_with_two += 1
        if char_counter(bid, verbosity)[1] == 1:
            if verbosity:
                print("triplicate in {0}".format(bid))
            boxids_with_three += 1
    multiplier = boxids_with_two * boxids_with_three
    return(multiplier)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
    parser.add_argument('--file', '-f', dest='file', help='please give me a file to read from')
    parser.add_argument('--verbose', '-v', action='count', help='let me know if you want to see more details')
    args = parser.parse_args()

    print(id_checker(args.file, args.verbose))







