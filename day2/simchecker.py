import argparse


def checker(input_file="", verbosity=""):
    boxids = open(input_file).readlines()
    boxids = [x.strip() for x in boxids]

    for bid in boxids:
        # bid = abcde
        for bidy in boxids:
            # bidy = zxcvb
            # bidy = asdfg
            if bid == bidy:
                if verbosity:
                    print("skipping {0} {1}".format(bid, bidy))
                continue
            counter = 0
            samesies = ""
            bida = []
            biday = []
            for b in bid:
                bida.append(b)
            for y in bidy:
                biday.append(y)
            ei = 0
            if verbosity:
                print("bida = {0}\nbiday = {1}".format(bida, biday))
            while ei <= 25:
                if bida[ei] == biday[ei]:
                    samesies += bida[ei]
                    counter += 1
                    if counter == 25:
                        return("samesies: {0}, bid: {1}, bidy: {2}".format(samesies, bid, bidy))
                ei += 1


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
    parser.add_argument('--file', '-f', dest='file', help='please give me a file to read from')
    parser.add_argument('--verbose', '-v', action='count', help='let me know if you want to see more details')
    args = parser.parse_args()

    print(checker(args.file, args.verbose))


