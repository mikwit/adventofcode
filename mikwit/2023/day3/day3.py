import sys
import argparse
from icecream import ic

# day2
from math import prod


# import heapq

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-r", "--real", action="store_true", help="whether to run with real data"
)
# parser.add_argument(i'file', '--file'. help='please give me a file to read from')
args = parser.parse_args()


def data_array(input_file="test-data.txt"):
    # def data_array(input_file="data.txt"):
    with open(input_file) as f:
        content = f.read().split("\n")
        # ic(content)

        # final_dict = {}
        # cur_elf = 1
        # for line in content:
        #     # ic(line)
        #     if line == '':
        #         cur_elf += 1
        #         continue
        #     if cur_elf in final_dict.keys():
        #         final_dict[cur_elf].append(line)
        #         # ic(final_dict)
        #     else:
        #         final_dict[cur_elf] = [line]
        #         # ic(final_dict)
        # # ic(final_dict)
        # # exit()
    f.close()
    return content
    # return final_dict


def build_games_dict(input_data, ic_enabled=True):
    if ic_enabled:
        ic.enable()
    else:
        ic.disable()

    games_dict = {}

    colors = ["red", "green", "blue"]

    for game in input_data:
        game_id = game.split(": ")[0].split(" ")[1]
        ic(game_id)

        pulls = game.split(": ")[1].split("; ")
        ic(pulls)

        # game_dict = {}
        game_array = []

        for pull in pulls:
            pull_dict = {}
            ic(pull)

            each_color_in_pull = pull.split(", ")
            ic(each_color_in_pull)

            for num_color in each_color_in_pull:
                cur_num, cur_color = num_color.split(" ")
                ic(cur_num, cur_color)

                pull_dict[cur_color] = int(cur_num)
                ic(pull_dict)

            game_array.append(pull_dict)

        ic(game_array)
        games_dict[game_id] = game_array

    ic(games_dict)

    ic.enable()

    return games_dict


def old_part_one(input_data):
    """
    Which games would have been possible if the bag contained:
        ONLY 12 red cubes, 13 green cubes, and 14 blue cubes?

        1, 2, and 5 from TEST would have been POSSIBLE
        3 would have been IMPOSSIBLE (20 red cubes at once)

    THEN, add up the IDs of the games that would have been possible
    TEST = 8
    """

    # ic(input_data)

    games_dict = build_games_dict(input_data, False)

    # ic(games_dict)

    max_values = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    possible_games = [game_id for game_id in games_dict]
    impossible_games = []
    # ic(possible_games)

    for game_id, game_pulls in games_dict.items():
        # ic(game_id, game_pulls)

        if game_id in possible_games:
            for pull in game_pulls:
                for pull_col, pull_val in pull.items():
                    if pull_val > max_values[pull_col]:
                        # ic(f"{pull_val} > {max_values[pull_col]}")
                        if game_id in possible_games:
                            possible_games.remove(game_id)
                        # else:
                        # ic(f"tried to remove {game_id} from {possible_games}")
                        if game_id not in impossible_games:
                            impossible_games.append(game_id)
                        # ic(possible_games)
                        # ic(impossible_games)
                        break
                # for color, max_val in max_values.items():
                # if pull[color] > max_val:
                # ic(f"{pull[color]} > {max_val}")
                # pass

    # ic(possible_games)
    # ic(impossible_games)

    sum_of_possible_game_ids = sum([int(game_id) for game_id in possible_games])
    # sum_of_possible_game_ids = sum(possible_games)
    print(f"day2 p1: {sum_of_possible_game_ids=}")

    return


def old_part_two(input_data):
    """
    What are the FEWEST # of EACH COLOR that could have made the game possible?
    """

    # from itertools import product

    games_dict = build_games_dict(input_data, False)

    # minimum_per_each_game_dict = {}
    power_per_game = {}

    for game_id, game_pulls in games_dict.items():
        minimum_per_cur_game = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        # ic(game_id, game_pulls)

        for pull in game_pulls:
            for pull_col, pull_val in pull.items():
                if pull_val > minimum_per_cur_game[pull_col]:
                    minimum_per_cur_game[pull_col] = pull_val
        # ic(minimum_per_cur_game)
        game_power = prod(minimum_per_cur_game.values())
        # ic(game_power)
        power_per_game[game_id] = game_power

    total_power = sum(power_per_game.values())
    print(f"day2 p2: {total_power=}")

    return



def full_part_number_finder(line, direction, starting_pos):

    max_position = len(line)-1

    if starting_pos == len(line)-1:
        # we are all the way right
        return line[starting_pos]
    elif starting_pos == 0:
        # we are all the way left
        return line[starting_pos]

    if direction == "left":
        pos_incrementer = -1
    elif direction == "right":
        pos_incrementer = 1

    pos_increment = pos_incrementer

    full_part_number = line[starting_pos]

    # if pos_increment + starting_pos == max_position+1:
    #     return line[starting_pos]
    # elif pos_increment + starting_pos == -1:
    #     return line[starting_pos]

    # if starting_pos + pos_increment == len(line)-1:
    #     # +1 right will be end of line
    #     pass
    # elif starting_pos + pos_increment == 0:
    #     # +1 left will be end of line
    #     pass

    # ic(f"starting position is {starting_pos}")
    # ic(f"starting number is {line[starting_pos]}")
    # ic(f"pos_increment is {pos_increment}")


    while line[starting_pos+pos_increment].isdigit():
        if direction == "left":
            # prepend
            full_part_number = line[starting_pos+pos_increment] + full_part_number
        elif direction == "right":
            full_part_number = full_part_number + line[starting_pos+pos_increment]
        pos_increment += pos_incrementer
        # ic(pos_increment)
        if starting_pos + pos_increment == len(line):
            break
        elif starting_pos + pos_increment == -1:
            break

        # if pos_increment + starting_pos == max_position-1:
        #     break
        # elif pos_increment + starting_pos == 1:
        #     break
    # ic(full_part_number)
    # sys.exit()
            # append

    return full_part_number


def part_one(input_data):
    """
    Need to add up all the part numbers in the engine schematic to see which part is missing
    
    Input data is a visual representation of the engine

    any number adjacent to a symbol,
        even diagonally,
    is a "part number"
    PERIODS ARE NOT SYMBOLS



    """

    cur_line_index = 0
    valid_part_numbers = []


    # if char is a number
    # check left, right, up, down, up-left, up-right, down-left, down-right
    # if any of those is a symbol, char is a valid number
    # if left char is a number, skip
    # if right char is a number, combine the strings



    # FIND ALL SYMBOLS AND THEIR POSITIONS
    symbol_dict = {}
    # line_number : [symbol_position_1, symbol_position_2]
    cur_line_index = 0
    for line in input_data:
        cur_char_index = 0
        for char in line:
            if not char.isdigit() and char != ".":
                # if symbol_dict[cur_line_index]:
                if cur_line_index in symbol_dict.keys():
                    # symbol_dict[cur_line_index] = symbol_dict[cur_line_index].append(cur_char_index)
                    symbol_dict[cur_line_index].append(cur_char_index)
                else:
                    symbol_dict[cur_line_index] = [cur_char_index]
            cur_char_index += 1
        cur_line_index += 1
    ic(symbol_dict)


    line_length = len(input_data[0])



    # FIND NUMBERS AROUND EACH SYMBOL
    for symbol_line, symbol_positions in symbol_dict.items():
        for symbol_position in symbol_positions:
            # ic(type(symbol_position))
            
            cur_line_text = input_data[symbol_line]
            
            # check if number to left of position, recursively?
            if symbol_position != 0:
                if cur_line_text[symbol_position-1].isdigit():

                    # ic(f"{cur_line_text[symbol_position-1]} is part of a valid part number!")

                    # starting position is a digit and is a partial part number
                    # please find full part number
                    full_part_number = full_part_number_finder(cur_line_text, "left", symbol_position-1)
                    valid_part_numbers.append(full_part_number)

                    # ic(f"{full_part_number} is a valid part number")

            # check if number to the right of position, recursively
            if symbol_position != line_length-1:
                if cur_line_text[symbol_position+1].isdigit():
                    # ic(f"{cur_line_text[symbol_position+1]} is part of a valid part number!")
                    # starting position is a digit and is a partial part number
                    # please find full part number
                    full_part_number = full_part_number_finder(cur_line_text, "right", symbol_position+1)
                    # ic(f"{full_part_number} is a valid part number")
                    valid_part_numbers.append(full_part_number)


            #TODO: in ABOVE and BELOW, fix it to check from directly above and below symbol instead of diagonally
            # check number above, unless it's top
            # ABOVE
            if symbol_line != 0:
                previous_line_text = input_data[symbol_line-1]
                # ic(previous_line_text)
                # check if number to left of position, recursively?
                if symbol_position != 0:
                    
                    if previous_line_text[symbol_position-1].isdigit():
                        ic("left above is digit")

                        # starting position is a digit and is a partial part number
                        # please find full part number
                        full_part_number = full_part_number_finder(previous_line_text, "left", symbol_position-1)
                        ic(f"need to add {full_part_number}")
                        valid_part_numbers.append(full_part_number)

                # check if number to the right of position, recursively
                if symbol_position != line_length-1:
                    if previous_line_text[symbol_position+1].isdigit():
                        ic("right above is digit")
                        # starting position is a digit and is a partial part number
                        # please find full part number
                        full_part_number = full_part_number_finder(previous_line_text, "right", symbol_position+1)
                        # ic(f"{full_part_number} is a valid part number")
                        valid_part_numbers.append(full_part_number)

            
            # check number below, unless it's bottom
            # BELOW
            if symbol_line != len(input_data):
                next_line_text = input_data[symbol_line-1]
                # ic(previous_line_text)
                # check if number to left of position, recursively?
                if symbol_position != 0:
                    
                    if next_line_text[symbol_position-1].isdigit():
                        ic("left above is digit")

                        # starting position is a digit and is a partial part number
                        # please find full part number
                        full_part_number = full_part_number_finder(next_line_text, "left", symbol_position-1)
                        ic(f"need to add {full_part_number}")
                        valid_part_numbers.append(full_part_number)

                # check if number to the right of position, recursively
                if symbol_position != line_length-1:
                    if next_line_text[symbol_position+1].isdigit():
                        ic("right above is digit")
                        # starting position is a digit and is a partial part number
                        # please find full part number
                        full_part_number = full_part_number_finder(next_line_text, "right", symbol_position+1)
                        # ic(f"{full_part_number} is a valid part number")
                        valid_part_numbers.append(full_part_number)

                pass

            # check if number in position in previous line
            # check if number in position in next line


    ic(f"{valid_part_numbers=}")

    # for line in input_data:
    #     # do i trust that a line is never repeated?
    #     # ic(input_data.index(line))

    #     cur_char_index = 0

    #     for char in line:
    #         if char.isdigit():
    #             ic(f"{char} is a digit")

    #             if cur_char_index != 0:
    #                 pass
    #             else:
    #                 if line[char-1].isdigit():
    #                     # check surrounding this one
    #                     pass
    #                 # while True:

    #                 # if line[char+1].isdigit()

    #             sys.exit()
    #         else:
    #             ic(f"{char} is not a digit")

    #         # ic(char)
    #         cur_char_index += 1
    #     # break
    #     cur_line_index += 1



    return


def part_two(input_data):
    """

    """
    return


def main():
    if args.real:
        data = data_array("data.txt")
    else:
        data = data_array("test-data.txt")
    # test a subset
    # data = data[:5]
    # data.append(479)
    # print(f"expenses = {expenses}")

    # total_calories_per_elf = get_calories_per_elf(data)
    # # ic(total_calories_per_elf)

    # # get_elf_with_highest_calories(total_calories_per_elf)
    # get_highest_calories(total_calories_per_elf)

    # get_three_highest_calories(total_calories_per_elf)

    # secret number of cubes in each bag
    # cubes are RED, GREEN, or BLUE
    # TODO: figure out info about # of cubes

    part_one(data)

    part_two(data)

    ic()

    # exit()

    # number_increased = find_increased_count(data)
    # print(f"increased count: {number_increased}")

    # number_increased_windows = increased_count_windows(data)
    # print(f"increased count windows: {number_increased_windows}")

    # pairs = find_2020_pairs(expenses)
    # print(f"products for 2 expenses that sum to 2020: {pairs}")

    # triples = find_2020_triples(expenses)
    # print(f"products for 3 expenses that sum to 2020: {triples}")

    return


if __name__ == "__main__":
    ic()
    # parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
    # parser.add_argument('--file', '-f', dest='file', help='please give me a file to read from')
    # parser.add_argument('--verbose', '-v', action='count', help='let me know if you want to see more details')
    # args = parser.parse_args()
    # print(dup_finder(args.file, args.verbose, 0))
    # print(file_duplicator(args.file, args.verbose, 0))

    main()
