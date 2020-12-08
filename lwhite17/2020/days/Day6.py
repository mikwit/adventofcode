import AoC_tools as AT


alphabet = 'abcdefghijklmnopqrstuvwxyz'


def any_yes(data):
    count_total = 0

    # count unique questions answered yes per group
    for group in data:
        group_chars = group.replace('\n', '')
        unique_chars = ''.join(set(group_chars))
        count_total += len(unique_chars)
    return count_total

def every_yes(data):
    count_total = 0

    for group in data:
        if '\n' in group:
            common_chars = []
            responses = group.split('\n')
            responses = [list(response) for response in responses if len(response) > 0]
            first = responses[0]

            for char in first:
                in_responses = [char in response for response in responses[1:]]
                # char must be in each response; should be no False values
                if False in in_responses:
                    pass
                else:
                    common_chars.append(char)
        else:
            common_chars = group
        count_total += len(common_chars)
    return count_total


def part_one(input_data):
    res = any_yes(input_data)
    print("\ntotal questions that received an answer of yes per group: ", res)


def part_two(input_data):
    res = every_yes(input_data)
    print("\ntotal number of questions that received a unanimous yes: ", res)


def both(input_data):
    res = any_yes(input_data)
    print("\ntotal questions that received an answer of yes per group: ", res)
    res = every_yes(input_data)
    print("total number of questions that received a unanimous yes: ", res)


if __name__ == '__main__':
    data = AT.load_txt(input("please enter data path: \n"), sep='\n\n')
    res = any_yes(data)
    print("\ntotal questions that received an answer of yes per group: ", res)
    res = every_yes(data)
    print("total number of questions that received a unanimous yes: ", res)
