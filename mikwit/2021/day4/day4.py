import sys

# import argparse

# parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
# parser.add_argument(i'file', '--file'. help='please give me a file to read from')
# args = parser.parse_args()

# 123456789012
# 000011110010

# def data_array(input_file="data.txt"):
#     with open(input_file) as f:
#         content = f.read().strip()
#         # print(f"{content}")
#         array_of_input = content.split('\n')
#         # print(f"{array_of_input}")

#         # for line in content:
#         # exit()
#         # 
#         # array_of_input = content.split()
#         # final_array = [int(each_int) for each_int in array_of_input]
#         # print(f"{final_array}")
#         # exit()
#     return array_of_input
#     # return final_array


def get_drawing_sequence(input_file="data.txt"):
    with open(input_file) as f:
        for line in f:
            array_of_input = line.split(',')

            final_array = [int(each_int) for each_int in array_of_input]
            # print(f"final_array = {final_array}")
            return final_array


def get_bingo_cards(input_file="data.txt"):
    with open(input_file) as f:
        i = 0
        card_number = 0
        bingo_cards = {}
        current_card_lines = []
        for bleh_line in f:
            if i < 2:
                i += 1
                continue

            line = bleh_line.strip()

            if any(map(str.isdigit, line)):
            # if line.contains_digit():
                current_card_lines.append(line)
            else:
                bingo_cards[card_number] = current_card_lines.copy()
                # print(f"bingo cards: {bingo_cards}")
                card_number += 1
                current_card_lines.clear()
                # print(f"bingo cards: {bingo_cards}")
                # print(f"card_number: {card_number}")
                # print(f"current_card_lines: {current_card_lines}")
                # print(f"i: {i}")
                # print(f"len: {len(bingo_cards)}")

            i += 1
    return bingo_cards




# for each bingo card
# generate winning combinations
# columns
# rows
# two diags

# after 5 numbers, search for any winning combinations containing those numbers


# def 

def get_winning_sequences(bingo_cards):
    winning_sequences = {}

    for card_number, card in bingo_cards.items():
        current_winning_sequences = []

        # print(f"card: {card}")

        # get rows, 5
        for line in card:
            line_array = line.split()
            current_winning_sequences.append(line_array)
            # print(f"row win: {line_array}")
        # print(f"current_winning_combos: {current_winning_sequences}")

        # get columns, 5
        column_index_range = len(card[0].split())
        for column_index in range(column_index_range):
            current_column_sequence = []
            for line in card:
                current_column_sequence.append(line.split()[column_index])
            current_winning_sequences.append(current_column_sequence)
            # print(f"column win: {current_column_sequence}")
        # print(f"current_winning_combos after columns: {current_winning_sequences}")

        # get diagonals, 2
        ### NEVERMIND
        ### I CAN'T READ
        ### DIAGONALS DON'T COUNT
        # current_diag_seq = []
        # current_diag_seq_2 = []
        # i = 0
        # j = 4
        # for line in card:
        #     current_diag_seq.append(line.split()[i])
        #     current_diag_seq_2.append(line.split()[j])
        #     i += 1
        #     j -= 1
        # print(f"diag1 win: {current_diag_seq}")
        # print(f"diag2 win: {current_diag_seq_2}")
        # current_winning_sequences.append(current_diag_seq)
        # current_winning_sequences.append(current_diag_seq_2)
        # print(f"current_winning_combos after diags: {current_winning_sequences}")

        winning_sequences[card_number] = current_winning_sequences
    # print(f"all winning sequences: {winning_sequences}")
    return winning_sequences




def play_bingo(drawing_sequence, bingo_cards):
    draws = []
    winning_sequences = get_winning_sequences(bingo_cards)
    for draw in drawing_sequence:
        draws.append(str(draw))
        if len(draws) > 3:
            for card, card_win_sequences in winning_sequences.items():
                for win_sequence in card_win_sequences:
                    # if all(draw_num in draws for win_num in win_sequence):
                    # print(f"seq: {draws}, win_seq: {win_sequence}")
                    # if set(win_sequence).issuperset(draws):
                    if set(draws).issuperset(win_sequence):
                        print(f"found it")
                        return (card, win_sequence, draw)
                    # else:
                        # print("no")

def play_bingo_to_lose(drawing_sequence, bingo_cards):
    draws = []
    winning_sequences = get_winning_sequences(bingo_cards)
    temp_cards = bingo_cards.copy()
    # print(f"temp cards: {temp_cards}")
    # exit()
    for draw in drawing_sequence:
        draws.append(str(draw))
        if len(draws) > 3:
            for card, card_win_sequences in winning_sequences.items():
                for win_sequence in card_win_sequences:
                    # # if all(draw_num in draws for win_num in win_sequence):
                    # print(f"seq: {draws}, win_seq: {win_sequence}")
                    # # if set(win_sequence).issuperset(draws):
                    if set(draws).issuperset(win_sequence):
                        if len(temp_cards.keys()) > 1:
                            # print(f"removing card")
                            if card in temp_cards.keys():
                                temp_cards.pop(card)
                            else:
                                pass
                        else:
                            # print(f"cards remaining: {temp_cards}")
                            if card in temp_cards.keys():
                                print(f"last winning card is {card}, {card_win_sequences}")
                                return (card, win_sequence, draw)

                        # temp_cards.pop(card)
                        # continue
                    # else:
                        # print("no")


            # return




def main():


    drawing_sequence = get_drawing_sequence()
    bingo_cards = get_bingo_cards()
    # print(f"{bingo_cards}")
    # data = data_array()

    winning_card, winning_sequence, last_number = play_bingo(drawing_sequence, bingo_cards)

    full_card = bingo_cards[winning_card]
    print(f"full_card: {full_card}")
    print(f"last_number: {last_number}")
    print(f"winning_seq: {winning_sequence}")

    draws_used = []
    for draw in drawing_sequence:
        if int(draw) != int(last_number):
            draws_used.append(int(draw))
        else:
            break
    draws_used.append(int(last_number))
    print(f"draws_used: {draws_used}")

    winning_card_sum = 0
    for ea_line in full_card:
        line = ea_line.split()
        for number in line:
            if int(number) not in draws_used:
                # print(f"{number} from card was not used in {draws_used}")
                winning_card_sum += int(number)
            # else:
                # print(f"{number} in draws {draws_used}")
    # for ea_number in winning_sequence:
        # winning_card_sum -= int(ea_number)
    print(f"winning_card_sum = {winning_card_sum}")

    print(f"! PART1 Answer: winning_card_sum * last_number_called = {winning_card_sum * int(last_number)}")




    winning_card, winning_sequence, last_number = play_bingo_to_lose(drawing_sequence, bingo_cards)

    full_card = bingo_cards[winning_card]
    print(f"full_card: {full_card}")
    print(f"last_number: {last_number}")
    print(f"winning_seq: {winning_sequence}")

    draws_used = []
    for draw in drawing_sequence:
        if int(draw) != int(last_number):
            draws_used.append(int(draw))
        else:
            break
    draws_used.append(int(last_number))
    print(f"draws_used: {draws_used}")

    winning_card_sum = 0
    for ea_line in full_card:
        line = ea_line.split()
        for number in line:
            if int(number) not in draws_used:
                # print(f"{number} from card was not used in {draws_used}")
                winning_card_sum += int(number)
            # else:
                # print(f"{number} in draws {draws_used}")
    # for ea_number in winning_sequence:
        # winning_card_sum -= int(ea_number)
    print(f"last_winning_card_sum = {winning_card_sum}")

    print(f"! PART2 Answer: last_winning_card_sum * last_number_called = {winning_card_sum * int(last_number)}")











    # product = 1
    # for number in winning_sequence:
    #     product = product * int(number)

    # # print(f"product of winning card's sequence = {(1 * int(number)) for number in winning_sequence}")
    # print(f"product of winning card's sequence: {product}")

    exit()
    
    # test a subset
    # data = data[:5]
    # data.append(479)
    # print(f"expenses = {expenses}")

    # final_position = plot_course(data)
    # print(f"final position (horizontal * vertical) = {final_position}")

    # final_correct_pos = plot_corrected_course(data)
    # print(f"final correct position (horizontal * vertical) = {final_correct_pos}")

    gamma = int(get_gamma(data), 2)
    # exit()
    epsilon = int(get_epsilon(data), 2)
    print(f"{gamma}")
    print(f"{epsilon}")
    # exit()
    print(f"gamma, epsilon, multiplied: {gamma}, {epsilon}, {gamma * epsilon}")
    o2 = int(get_o2(data), 2)
    print(f"o2: {o2}")

    co2 = int(get_co2(data), 2)
    print(f"co2: {co2}")

    print(f"o2 * c02 = {o2 * co2}")
    # print(f"final position (horizontal * vertical) = {final_position}")


    return


if __name__ == "__main__":

    # parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
    # parser.add_argument('--file', '-f', dest='file', help='please give me a file to read from')
    # parser.add_argument('--verbose', '-v', action='count', help='let me know if you want to see more details')
    # args = parser.parse_args()
    # print(dup_finder(args.file, args.verbose, 0))
    # print(file_duplicator(args.file, args.verbose, 0))

    main()
