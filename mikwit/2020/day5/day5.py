import sys


def get_data(datafile):
    with open(datafile) as f:
        data = f.read().split('\n')
        # print(f"read_data is: {read_data}")
    return data


def get_row(row_info):
    rows = list(range(0,128))
    # print(f"rows: {rows}")

    for operator in row_info:
        if operator == "F":
            rows = rows[:len(rows)//2]
        elif operator == "B":
            rows = rows[len(rows)//2:]
        else:
            print(f"failure, expected F or B: {operator}")
            sys.exit()
        # print(f"remaining rows is: {rows}")
    # print(f"the row is: {rows}")
    return rows[0]


def get_column(column_info):
    columns = list(range(0,8))

    for operator in column_info:
        if operator == "L":
            columns = columns[:len(columns)//2]
        elif operator == "R":
            columns = columns[len(columns)//2:]
        else:
            print(f"failure, expected L or R: {operator}")
            sys.exit()
    # print(f"the column is: {columns}")
    return columns[0]


def find_seat_ids(boarding_passes):
    seat_id_array = []

    for boarding_pass in boarding_passes:
        row = get_row(boarding_pass[:7])
        column = get_column(boarding_pass[7:])
        seat_id = row * 8 + column
        seat_id_array.append(seat_id)
    # print(f"all seat ids: {seat_id_array}")
    # max_seat_id = max(seat_id_array)
    return seat_id_array


def find_my_seat(seat_id_array, max_seat_id):
    existing_seat_ids = list(range(0, max_seat_id))
    for seat in existing_seat_ids:
        if seat not in seat_id_array:
            if (seat - 1) in seat_id_array and (seat + 1) in seat_id_array:
                return seat
                # print(f"missing seat id {seat}")
    print("couldn't finding my seat")
    sys.exit()


if __name__ == "__main__":
    # boarding_data_array = get_data("testdata.txt")
    boarding_data_array = get_data("data.txt")
    # print(f"boarding_data: {boarding_data_array}")

    seat_ids = find_seat_ids(boarding_data_array)
    # print(f"all seat ids: {seat_ids}")

    highest_seat_id = max(seat_ids)
    print(f"highest seat id: {highest_seat_id}")

    my_seat = find_my_seat(seat_ids, highest_seat_id)
    print(f"my seat is {my_seat}")
