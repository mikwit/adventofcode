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
            # create new card / array
            current_card = np.zeros((5, 5))
        elif ind % 5 == 4:
            # add finished card (array) to list of cards (arrays)
            bingo_cards.append(current_card)
        # add line to array
        current_card[ind % 5, :] = int_line

    return number_draws, bingo_cards


def call_first_winner(number_draws, bingo_cards):
    for ind, call in enumerate(number_draws):
        for card_ind, card in enumerate(bingo_cards):
            # check if called values complete any rows/columns of each card
            row_status = np.isin(card, number_draws[:ind+1]).all(axis=1)
            col_status = np.isin(card, number_draws[:ind+1]).all(axis=0)
            if row_status.any() or col_status.any():
                return card, call


def part_one(data, number_draws=None, bingo_cards=None):
    if not number_draws and not bingo_cards:
        if type(data[0]) == str:
            number_draws, bingo_cards = format_data(data=data)
    winning_card, call = call_first_winner(number_draws=number_draws, bingo_cards=bingo_cards)

    # score winning card
    card_sum = winning_card.sum()
    call_sum = winning_card[np.isin(winning_card, number_draws[:number_draws.index(call)+1])].sum()
    return (card_sum-call_sum) * call


def call_last_winner(number_draws, bingo_cards):
    done_cards = []
    for ind, call in enumerate(number_draws):
        for card_ind, card in enumerate(bingo_cards):
            # check if called values complete any rows/columns of each card
            row_status = np.isin(card, number_draws[:ind + 1]).all(axis=1)
            col_status = np.isin(card, number_draws[:ind + 1]).all(axis=0)
            if row_status.any() or col_status.any():
                # add winning card to list of winning cards until all win
                if card_ind in done_cards:
                    continue
                else:
                    done_cards.append(card_ind)
                if len(done_cards) == len(bingo_cards):
                    # get index of last card that won
                    last_card = done_cards[-1]
                    return bingo_cards[last_card], call


def part_two(data, number_draws=None, bingo_cards=None):
    if not number_draws and not bingo_cards:
        if type(data[0]) == str:
            number_draws, bingo_cards = format_data(data=data)
    losing_card, call = call_last_winner(number_draws=number_draws, bingo_cards=bingo_cards)

    # score losing card
    card_sum = losing_card.sum()
    call_sum = losing_card[np.isin(losing_card, number_draws[:number_draws.index(call)+1])].sum()
    return (card_sum-call_sum) * call


def both(data):
    number_draws, bingo_cards = format_data(data=data)
    print("Score of first winning board is: " + str(part_one(data=data, number_draws=number_draws,
                                                             bingo_cards=bingo_cards)))
    print("Score of last winning board is: " + str(part_two(data=data, number_draws=number_draws,
                                                            bingo_cards=bingo_cards)))


if __name__ == '__main__':
    if input("Use pre-loaded data?\n") in ['y', 'Y', 'yes', 'Yes', 'YES']:
        use_data = load_txt('Data.txt')
    else:
        use_data = load_txt(input("please enter data path: \n"))

    # test using sample data
    # use_data = load_txt('SampleData.txt')
    both(data=use_data)
