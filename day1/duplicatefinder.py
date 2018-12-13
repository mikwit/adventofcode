# import sys
import argparse

# parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
# parser.add_argument(i'file', '--file'. help='please give me a file to read from')
# args = parser.parse_args()




def file_summator(input_file="", current_number=0):
    in_file = open(input_file, "r")
    total = current_number
    for line in in_file:
        total += int(line)
    return(int(total))




def file_duplicator(input_file="", verbosity="", current_number=0):

    offset = file_summator(input_file, current_number)





    in_file = open(input_file, "r")
    total = current_number
    array = []

    numberarray = []

    for each_number in in_file:
        numberarray.append(int(each_number))

    if verbosity:
        print("offset == {}".format(offset))

    # for line in in_file:
    #     modulus = int(line) % offset
    #     omodulus = offset % int(line)
    #     # if int(line) != offset and modulus == 0:
    #     #     print("line {0} % offset {1} == 0".format(line, offset))
    #     #     return(int(line))
    #     # if int(line) != offset and offset % int(line) == 0:
    #     #     print("offset {0} % line {1} == 0".format(offset, line))
    #     #     return(line)


    #     total += int(line)
    #     if total == offset:
    #         print("total == offset, line = {}" .format(line))
    #         for line in in_file:
    #             if int(line) % offset == 0:
    #                 return(line)
    #         # return(line)
    #     if total not in array:
    #         array.append(total)
    #     else:
    #         return(total)

    fr_total = 0
    firstresults = []
    for fr_en in numberarray:
        fr_total += int(fr_en)
        firstresults.append(fr_total)


    # print(firstresults)
    # return

    no = 1
    current_array = firstresults.copy()
    while no == 1:
        if verbosity:
            print("current_array: {}".format(current_array))
        for enca in current_array:
            index = current_array.index(enca)
            if verbosity:
                print("index: {0} --- value: {1}".format(index, current_array[index]))
            current_array[index] = firstresults[index] + offset
            # current_array[current_array.index(enca)] = firstresults[firstresults.index(enca)] + offset
            if verbosity:
                print("current item: {0}, new item: {1}".format(enca, current_array[index]))
                # print("current item: {0}, new item: {1}".format(enca, current_array[current_array.index(enca)]))
            # if current_array[current_array.index(enca)] in firstresults:
            if current_array[index] in firstresults:
                if verbosity:
                    print("I found value {0} in {1}".format(current_array[index], firstresults))
                no = 0
                return(current_array[index])
                # return(current_array[current_array.index(enca)])


#     nottrue = 1
#     tester = 0
#     while nottrue == 1:
#         tester += 1
#         if verbosity:
#             print("loop number: {}".format(tester))
#         for en in numberarray:
#             if verbosity:
#                 print("en: {}".format(en))
#             total += int(en)
#             # print("total: {}".format(total))
#             # print("en: {}".format(en))
#             if total not in array:
#                 array.append(total)
#                 # array.sort()
#                 if verbosity:
#                     print("array: {}".format(array))
#             else:
#                 if verbosity:
#                     print("array: {} END".format(array))
#                 nottrue = 0
#                 return(total)
#             # total = int(en)
#     # return(total)



# 
#     nottrue = 1
#     tester = 0
#     while nottrue == 1:
#         tester += 1
#         print("loop number: {}".format(tester))
#         for line in in_file:
#             print("line: {}".format(line))
#             total += int(line)
#             # print("total: {}".format(total))
#             # print("line: {}".format(line))
#             if total not in array:
#                 array.append(total)
#                 # array.sort()
#                 print("array: {}".format(array))
#             else:
#                 print("array: {} END".format(array))
#                 nottrue = 0
#                 return(total)
#             # total = int(line)
#     # return(total)




# print(file_duplicator("test.txt", 0))
# print(file_duplicator("input.txt", 0))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
    parser.add_argument('--file', '-f', dest='file', help='please give me a file to read from')
    parser.add_argument('--verbose', '-v', action='count', help='let me know if you want to see more details')
    args = parser.parse_args()
    print(file_duplicator(args.file, args.verbose, 0))

