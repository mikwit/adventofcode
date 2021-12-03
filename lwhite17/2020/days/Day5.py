import AoC_tools as AT


def process_passes(data):
    seats = []

    for seat in data:
        row = -1
        col = -1
        # list all possible row and column numbers
        rows = list(range(0, 128))
        cols = list(range(0, 8))

        for charInd, char in enumerate(seat):
            # if last B/F is F, take smaller row number. If B, larger.
            if charInd == 6:
                if char == 'F':
                    row = min(rows)
                else:
                    row = max(rows)
            # if last L/R is L, take smaller col number. If R, larger.
            elif charInd == 9:
                if char == 'L':
                    col = min(cols)
                else:
                    col = max(cols)

            # if character is F, keep bottom half of row columns
            if char == 'F':
                halflen = len(rows) / 2
                rows = rows[:int(halflen)]
            # if character is B, keep top half of row columns
            if char == 'B':
                halflen = len(rows) / 2
                rows = rows[int(halflen):]
            # if character is L, keep bottom half of col columns
            if char == 'L':
                halflen = len(cols) / 2
                cols = cols[:int(halflen)]
            # if character is R, keep top half of col columns
            if char == 'R':
                halflen = len(cols) / 2
                cols = cols[int(halflen):]

        seatID = row * 8 + col
        seats.append(seatID)

    return seats


def highest_seat_id(data):
    seats = process_passes(data)
    return max(seats)


def missing_seat_id(data):
    seats = process_passes(data)
    # order seats in ascending order
    seats.sort()
    highest_seat = max(seats)

    my_seat = -1
    prev_seat = 0
    # after first filled seat, first and only skipped seat is mine
    for seat in seats:
        if prev_seat != 0:
            if seat - prev_seat == 2:
                my_seat = seat - 1
                break
        prev_seat = seat
    return my_seat


def part_one(input_data):
    res = highest_seat_id(input_data)
    print("\nhighest seat ID: ", res)


def part_two(input_data):
    res = missing_seat_id(input_data)
    print("\nyour seat, by process of elimination: ", res)


def both(input_data):
    res = highest_seat_id(input_data)
    print("\nhighest seat ID: ", res)
    res = missing_seat_id(input_data)
    print("your seat, by process of elimination: ", res)


if __name__ == '__main__':
    data = AT.load_txt(input("please enter data path: \n"), sep='\n')

    res = highest_seat_id(data)
    print("\nhighest seat ID: ", res)
    res = missing_seat_id(data)
    print("your seat, by process of elimination: ", res)
