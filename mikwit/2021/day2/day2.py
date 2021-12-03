import sys

# import argparse

# parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
# parser.add_argument(i'file', '--file'. help='please give me a file to read from')
# args = parser.parse_args()


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


def plot_course(data):

    depth = 0
    horizontal_pos = 0

    for line in data:
        direction, str_distance = line.split()
        # print(f"direction: {direction}, distance: {distance}")

        distance = int(str_distance)


        if direction == 'forward':
            horizontal_pos += distance
            # print(f"now at distance {horizontal_pos}")
        elif direction == 'up':
            depth -= distance
            # print(f"now at depth {depth}")
        elif direction == 'down':
            depth += distance
            # print(f"now at depth {depth}")
        else:
            print(f"uh oh!")

    print(f"final horizontal_pos: {horizontal_pos}, final depth: {depth}")

        # exit()
    return (depth * horizontal_pos)


def plot_corrected_course(data):

    depth = 0
    horizontal_pos = 0
    aim = 0

    for line in data:
        direction, str_distance = line.split()
        # print(f"direction: {direction}, distance: {distance}")

        distance = int(str_distance)

        if direction == 'forward':
            horizontal_pos += distance
            if aim > 0:
                depth += (aim * distance)
            else:
                depth -= (aim * distance)
            # print(f"now at distance {horizontal_pos}")
            # print(f"now at depth {depth}")
        elif direction == 'up':
            aim -= distance
            # print(f"now aiming {aim}")
        elif direction == 'down':
            aim += distance
            # print(f"now aiming {aim}")
        else:
            print(f"uh oh!")

    print(f"final horizontal_pos: {horizontal_pos}, final depth: {depth}")

        # exit()
    return (depth * horizontal_pos)



def main():
    data = data_array()
    # test a subset
    # data = data[:5]
    # data.append(479)
    # print(f"expenses = {expenses}")

    final_position = plot_course(data)
    print(f"final position (horizontal * vertical) = {final_position}")

    final_correct_pos = plot_corrected_course(data)
    print(f"final correct position (horizontal * vertical) = {final_correct_pos}")

    return


if __name__ == "__main__":

    # parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
    # parser.add_argument('--file', '-f', dest='file', help='please give me a file to read from')
    # parser.add_argument('--verbose', '-v', action='count', help='let me know if you want to see more details')
    # args = parser.parse_args()
    # print(dup_finder(args.file, args.verbose, 0))
    # print(file_duplicator(args.file, args.verbose, 0))

    main()
