import sys


def get_data(datafile):
    with open(datafile) as f:
        data = f.read().split('\n')
        # print(f"read_data is: {read_data}")
    return data


def join_group_answers(customs_data_array):
    counter = 0
    answers = {}
    for answer in customs_data_array:
        if not answer:
            counter += 1
        else:
            if counter in answers.keys():
                answers[counter] = answers[counter] + answer
            else:
                answers[counter] = answer
    group_answers = []
    for each_group_id in answers.keys():
        group_answers.append(answers[each_group_id])
    return group_answers


def get_group_sums(group_answers):
    group_sums = []
    for group in group_answers:
        # counter = 0
        group_sum = 0
        checked_chars = []
        for each_char in group:
            # counter += 1
            if each_char not in checked_chars:
                checked_chars.append(each_char)
        group_sums.append(len(checked_chars))
    return group_sums


def part2_join_group_answers(customs_data_array):
    counter = 0
    answers = {}
    for answer in customs_data_array:
        if not answer:
            counter += 1
        else:
            if counter in answers.keys():
                answers[counter] = answers[counter] + ' ' + answer
            else:
                answers[counter] = answer
    print(f"answers: {answers}")

    for each_group_id in answers.keys():
        group_answers_array = answers[each_group_id].split(' ')
        print(f"{each_group_id} answers: {group_answers_array}")
        answers[each_group_id] = group_answers_array
    return answers


def part2_get_group_sums(part2_group_answers_dict):
    print(f"part2: get group sums")
    group_sums = []
    for group in part2_group_answers_dict.keys():
        group_sum = 0
        counter = 0
        current_answers = part2_group_answers_dict[group]
        number_of_group_answers = len(current_answers)
        if number_of_group_answers == 1:
            group_sum = len(current_answers[counter])
            group_sums.append(group_sum)
        else:
            all_group_chars = []
            for answer in current_answers:
                for ea_char in answer:
                    if ea_char not in all_group_chars:
                        all_group_chars.append(ea_char)
            print(f"all_group_chars: {all_group_chars}")

            group_sum = len(all_group_chars)
            chars_not_universal = []
            for answer in current_answers:
                print(f"checking {answer}")
                for ea_char in all_group_chars:
                    print(f"    checking {ea_char} in {answer}")
                    if ea_char not in answer and ea_char not in chars_not_universal:
                        print(f"        {ea_char} not in {answer} from {current_answers}")
                        print(f"        decreasing group_sum")
                        # chars_in_all_answers.remove(ea_char)
                        group_sum -= 1
                        chars_not_universal.append(ea_char)
            print(f"group_sum is: {group_sums}")
            group_sums.append(group_sum)
        print(f"group_sums: {group_sums}")
    return group_sums


if __name__ == "__main__":
    # customs_data_array = get_data("testdata.txt")
    customs_data_array = get_data("data.txt")
    # print(f"boarding_data: {boarding_data_array}")

    group_answers = join_group_answers(customs_data_array)

    group_sums = get_group_sums(group_answers)
    print(f"group sums: {group_sums}")

    total_sum = 0
    for each_sum in group_sums:
        total_sum += each_sum
    print(f"total sum: {total_sum}")

    part2_group_answers_dict = part2_join_group_answers(customs_data_array)

    part2_group_sums = part2_get_group_sums(part2_group_answers_dict)

    total_sum = 0
    for each_sum in part2_group_sums:
        total_sum += each_sum
    print(f"part2 total sum: {total_sum}")
