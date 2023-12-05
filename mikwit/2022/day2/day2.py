import sys
from icecream import ic
# import heapq

# import argparse

# parser = argparse.ArgumentParser(description='take input file and find duplicate frequencies')
# parser.add_argument(i'file', '--file'. help='please give me a file to read from')
# args = parser.parse_args()


# def data_array(input_file="test-data.txt"):
def data_array(input_file="data.txt"):
    with open(input_file) as f:
        content = f.read().split('\n')
        # ic(content)
    f.close()
    return content
    # return final_dict


def get_total_score(data):
    ic()

    score = 0

    """
    # opponent
    A = Rock = 1
    B = Paper = 2
    C = Scissors = 3
    # me
    X = Rock = 1
    Y = Paper = 2
    Z = Scizzors = 3

    Win = 6
    Draw = 3
    Loss = 0
    """

    score_sneaky = 0

    for round in data:

        opponent, me = round.split(" ")
        # ic(opponent, me)

        outcome_points = play_game(opponent, me)
        # ic(outcome_points)

        if me == "X":
            played_points = 1
        elif me == "Y":
            played_points = 2
        elif me == "Z":
            played_points = 3
        
        score = score + played_points + outcome_points

        play_game_sneaky_score = play_game_sneaky(opponent, me)
        # ic(play_game_sneaky_score)

        score_sneaky = score_sneaky + play_game_sneaky_score

    ic(score)
    ic(score_sneaky)
    ic()
    return


def play_game(opponent, me):
    if opponent == "A":
        if me == "X":
            return 3
        if me == "Y":
            return 6
        if me == "Z":
            return 0
    elif opponent == "B":
        if me == "X":
            return 0
        if me == "Y":
            return 3
        if me == "Z":
            return 6
    elif opponent == "C":
        if me == "X":
            return 6
        if me == "Y":
            return 0
        if me == "Z":
            return 3
    else:
        ic(opponent, me)
        print(f"no match!!")
        exit()


def play_game_sneaky(opponent, me):
    if opponent == "A": # rock
        if me == "X":
            # NEED LOSE - scissors (3) + lose (0) 
            return 3
        if me == "Y":
            # NEED DRAW - rock (1) + draw (3)
            return 4
        if me == "Z":
            # NEED WIN - paper (2) + win (6)
            return 8
    elif opponent == "B": # paper
        if me == "X":
            # NEED LOSE - rock (1) + lose (0)
            return 1
        if me == "Y":
            # DRAW - paper (2) + draw (3)
            return 5
        if me == "Z":
            # WIN - scissors (3) + win (6)
            return 9
    elif opponent == "C": # scissors
        if me == "X":
            # LOSE - paper (2) + lose (0)
            return 2
        if me == "Y":
            # DRAW - scissors (3) + draw (3)
            return 6
        if me == "Z":
            # WIN - rock (1) + win (6)
            return 7
    else:
        ic(opponent, me)
        print(f"no match!!")
        exit()


def main():
    data = data_array()

    get_total_score(data)

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
