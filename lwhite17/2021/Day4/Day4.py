import numpy as np


def load_txt(filename, sep=None, ignore_empties=True, convert_to_type=None):
    if sep is None:
        sep = '\n'
    with open(r'' + filename, 'r') as f:
        results = f.read().split(sep)

    if ignore_empties:
        for element in results:
            if len(element) == 0:
                results.remove(element)

    if convert_to_type == 'int':
        for ind, element in enumerate(results):
            results[ind] = int(element)

    return results


def format_data(data):
    number_draws = data[0]
    number_draws = number_draws.split(",")
    number_draws = list(map(float, number_draws))

    bingo_cards = []
    current_card = np.zeros((5, 5))

    for ind, line in enumerate(data[1:]):
        # convert str line into int list
        int_line = list(map(float, line.split()))

        if ind % 5 == 0:
            current_card = np.zeros((5, 5))
        elif ind % 5 == 4:
            bingo_cards.append(current_card)
        current_card[ind % 5, :] = int_line

    return number_draws, bingo_cards


def call_bingo(number_draws, bingo_cards):
    for ind, call in enumerate(number_draws):
        for card in bingo_cards:
            row_status = np.isin(card, number_draws[:ind+1]).all(axis=1)
            col_status = np.isin(card, number_draws[:ind+1]).all(axis=0)

            pass

            if row_status.any():
                return card, call

            if col_status.any():
                return card, call


def part_one(data, number_draws=None, bingo_cards=None):
    if not number_draws and not bingo_cards:
        if type(data[0]) == str:
            number_draws, bingo_cards = format_data(data=data)
    winning_card, call = call_bingo(number_draws=number_draws, bingo_cards=bingo_cards)

    card_sum = winning_card.sum()
    call_sum = sum(number_draws[:number_draws.index(call)+1])

    return (card_sum-call_sum) * call


def part_two(data, number_draws=None, bingo_cards=None):
    if not number_draws and not bingo_cards:
        if type(data[0]) == str:
            number_draws, bingo_cards = format_data(data=data)
    return 0


def both(data):
    number_draws, bingo_cards = format_data(data=data)
    print("Score of winning board is: " + str(part_one(data=data, number_draws=number_draws,
                                                       bingo_cards=bingo_cards)))

    return 0


if __name__ == '__main__':
    # if input("Use pre-loaded data?\n") in ['y', 'Y', 'yes', 'Yes', 'YES']:
    #     use_data = load_txt('Data.txt')
    # else:
    #     use_data = load_txt(input("please enter data path: \n"))

    # example data

    # use_data = [[7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1],
    #
    #             22, 13, 17, 11, 0,
    #             8, 2, 23, 4, 24,
    #             21, 9, 14, 16, 7,
    #             6, 10, 3, 18, 5,
    #             1, 12, 20, 15, 19,
    #
    #             3, 15, 0, 2, 22,
    #             9, 18, 13, 17, 5,
    #             19, 8, 7, 25, 23,
    #             20, 11, 10, 24, 4,
    #             14, 21, 16, 12, 6,
    #
    #             14, 21, 17, 24, 4,
    #             10, 16, 15, 9, 19,
    #             18, 8, 23, 26, 20,
    #             22, 11, 13, 6, 5,
    #             2, 0, 12, 3, 7]

    use_data = load_txt('SampleData.txt')
    # use_data = load_txt('Data.txt')
    both(data=use_data)
