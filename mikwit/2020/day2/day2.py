# goal: let mom shadow "starting from scratch"


def count_actual_valid_passwords(input_data):

    valid_password_count = 0

    for line in input_data.split("\n"):
        # print(f"line is: {line}")
        line_array = line.split(":")
        # print(f"line_array is: {line_array}")
        policy = line_array[0]
        password = line_array[1]

        # figure out what the policy is
        #     each char represents position in string, total 2 positions
        #     if one and only one position contains the letter, then valid

        position_one = int(policy.split("-")[0])

        position_two_with_garbage = policy.split("-")[1]
        position_two = int(position_two_with_garbage.split(" ")[0])
        # print(f"policy_max is {policy_max}")
        # print(f"policy_max variable type is: {type(policy_max)}")
        policy_char = policy.split(" ")[1]
        # print(f"policy_char is {policy_char}")

        # check password
        char_one = password[position_one]
        char_two = password[position_two]

        valid_chars = 0

        if char_one == policy_char:
            valid_chars += 1
        if char_two == policy_char:
            valid_chars += 1

        if valid_chars == 1:
            valid_password_count += 1

    return valid_password_count


def count_valid_passwords(input_data):

    valid_password_count = 0

    for line in input_data.split("\n"):
        # print(f"line is: {line}")
        line_array = line.split(":")
        # print(f"line_array is: {line_array}")
        policy = line_array[0]
        password = line_array[1]
        # print(f"policy is: {policy}, password is: {password}")

        # figure out what the policy is
        policy_min = int(policy.split("-")[0])
        # print(f"policy_min is {policy_min}")
        policy_max_with_garbage = policy.split("-")[1]
        policy_max = int(policy_max_with_garbage.split(" ")[0])
        # print(f"policy_max is {policy_max}")
        # print(f"policy_max variable type is: {type(policy_max)}")
        policy_char = policy.split(" ")[1]
        # print(f"policy_char is {policy_char}")

        # check password
        # count number of policy_char in password
        char_count = password.count(policy_char)
        # print(f"the letter {policy_char} occurs {char_count} times in {password}")

        if char_count >= policy_min:
            if char_count <= policy_max:
                valid_password_count = valid_password_count + 1
        # print(f"valid count is: {valid_password_count}")
        # check if policy_char >= policy_min
        # check if policy_char IS ALSO <= policy_max

    return valid_password_count


def get_password_data():
    with open("data.txt") as f:
        read_data = f.read()
        # print(f"read_data is: {read_data}")
    return read_data


def run_the_program():

    password_data = get_password_data()

    if password_data:
        print("I have the data")
    else:
        print("I have NO DATA")

    # print(f"password_data is: {password_data}")

    number_of_valid_passwords = count_valid_passwords(password_data)

    # print("the answer is:")
    print(f"number of valid passwords is: {number_of_valid_passwords}")

    number_of_actual_valid_passwords = count_actual_valid_passwords(password_data)
    print(f"number of actual valid passwords is: {number_of_actual_valid_passwords}")


run_the_program()
