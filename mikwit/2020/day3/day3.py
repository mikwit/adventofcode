def get_data(datafile):
    with open(datafile) as f:
        data = f.read().split('\n')
        # print(f"read_data is: {read_data}")
    return data


def count_trees_on_any_path(tree_map, right_increment, row_increment):
    position = 0
    increment = right_increment
    next_row_increment = row_increment
    # print(f"{position}")

    tree_count = 0

    for row in tree_map:
        current_row_index = tree_map.index(row)
        # print(f"row: {row}")

        if current_row_index >= len(tree_map) - next_row_increment:
            break

        if current_row_index % next_row_increment != 0:
            continue

        next_row = tree_map[current_row_index + next_row_increment]
        # print(f"next row: {next_row}")

        position = position + increment

        # if position > len(next_row):
        while position > len(next_row) - 1:
            next_row += next_row

        if next_row[position] == '#':
            tree_count += 1

        # is_tree = get_next_pos()

    # print(f"tree count is {tree_count}")

    return tree_count


def count_trees_on_path(tree_map):
    position = 0
    increment = 3
    next_row_increment = 1
    print(f"{position}")

    tree_count = 0

    for row in tree_map:
        current_row_index = tree_map.index(row)
        # print(f"row: {row}")

        if current_row_index >= len(tree_map) - 1:
            break

        next_row = tree_map[current_row_index + next_row_increment]
        # print(f"next row: {next_row}")

        position = position + increment

        # if position > len(next_row):
        while position > len(next_row):
            next_row += next_row

        if next_row[position] == '#':
            tree_count += 1

        # is_tree = get_next_pos()

    print(f"tree count is {tree_count}")

    return


if __name__ == "__main__":

    tree_map = get_data("data.txt")
    # print(f"tree_map:\n{tree_map}")

    count_trees_on_path(tree_map)

    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]

    tree_counts = []
    for slope in slopes:
        # print(f"slope: {slope}")
        tree_counts.append(count_trees_on_any_path(tree_map, slope[0], slope[1]))
    print(f"tree_counts: {tree_counts}")
    tree_multiple = 1
    for tree_count in tree_counts:
        tree_multiple = tree_multiple * tree_count
    print(f"all trees: {tree_multiple}")