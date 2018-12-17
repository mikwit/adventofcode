import argparse


def dup_char_checker(boxid="", verbosity=""):
    boxid = boxid
    
    seen = []

    count = []


    tick = 0
    for b in boxid:
        if b not in seen:
            seen.append(b)
            count.append(dict(char=b, count=1))
            tick += 1
        else:
            # print("duplicate in seen: {0} - {1}" .format(seen.index(b), seen[seen.index(b)]))
            # # new_count = count[tick]
            # # print("duplicate in {}".format(count[tick]))
            # print("location in count: index {}".format(seen.index(b)))

            # new_count = count[seen.index(b)]['count'] + 1

            count[seen.index(b)]['count'] = count[seen.index(b)]['count'] + 1

            # print("current count: {0}, new count: {1}".format(count[seen.index(b)], "test"))
            # print("current count: {0}, new count: {1}".format(count[seen.index(b)]['count'], new_count))

    if verbosity:
        print("count: {0}".format(count))
        print("")


    return(count)



def id_checker(input_file="", verbosity=""):
    # in_file = open(input_file, "r")
    boxids = open(input_file).readlines()
    boxids = [x.strip() for x in boxids]

    if verbosity:
        print("boxids: {}".format(boxids))
        print("")


    results = []


    for bid in boxids:
        results.append(dict(boxid=bid, results=dup_char_checker(bid, verbosity)))

    if verbosity:

        print("\n\n\n")
        print("full results: {}".format(results))

    # for bid in boxids:
    #     seen = []
    #     if verbosity:
    #         print("bid: {0}".format(bid))
    #     for char in bid:
    #         if char not in seen:
    #             seen.append(char)
    #             if verbosity:
    #                 print("seen: {}".format(seen))
    #         else:
    #             results.append(dict(bid=char))
    #             if verbosity:
    #                 print("results: {}".format(results))




    return(boxids)












if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
    parser.add_argument('--file', '-f', dest='file', help='please give me a file to read from')
    parser.add_argument('--verbose', '-v', action='count', help='let me know if you want to see more details')
    args = parser.parse_args()


    print(id_checker(args.file, args.verbose))
    # print(dup_finder(args.file, args.verbose, 0))


    # print(file_duplicator(args.file, args.verbose, 0))







