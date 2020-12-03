def get_password_data():
    with open("data.txt") as f:
        read_data = f.read()
        # print(f"read_data is: {read_data}")
    return read_data


def count_valid_passwords(password_data):
    valid_password_count = 0

    for password_policy_line in password_data.split("\n"):
        # print(f"current line is: {password_policy_line}")

        password_policy_array = password_policy_line.split(":")
        # print(f"password_policy_array is: {password_policy_array}")

        policy = password_policy_array[0]
        password = password_policy_array[1]
        # print(f"policy is: {policy}, password is: {password}")

        # figure out what the policy is
        policy_min = int(policy.split("-")[0])
        # print(f"policy_min is {policy_min}")

        policy_max_with_garbage = policy.split("-")[1]
        policy_max = int(policy_max_with_garbage.split(" ")[0])
        # print(f"policy_max is {policy_max}")

        policy_char = policy.split(" ")[1]
        # print(f"policy_char is {policy_char}")

        # count number of policy_char in password
        char_count = password.count(policy_char)
        # print(f"the letter {policy_char} occurs {char_count} times in {password}")

        if char_count >= policy_min:
            if char_count <= policy_max:
                valid_password_count = valid_password_count + 1
                # print(f"valid count is: {valid_password_count}")
        # print(f"valid count is: {valid_password_count}")

    return valid_password_count


def count_actual_valid_passwords(password_data):
    valid_password_count = 0

    for password_policy_line in password_data.split("\n"):
        # print(f"current line is: {password_policy_line}")

        password_policy_array = password_policy_line.split(":")
        # print(f"password_policy_array is: {password_policy_array}")

        policy = password_policy_array[0]
        password = password_policy_array[1]

        # figure out what the policy is
        #     each char represents position in string, total 2 positions
        #     if one and only one position contains the letter, then valid
        #     NOTE: don't need to subtract 1 for indexing password, because char0 is " "
        position_one = int(policy.split("-")[0])

        position_two_with_space = policy.split("-")[1]
        position_two = int(position_two_with_space.split(" ")[0])
        # print(f"policy_max is {policy_max}")
        # print(f"policy_max variable type is: {type(policy_max)}")

        policy_char = policy.split(" ")[1]
        # print(f"policy_char is {policy_char}")

        # check password pieces
        char_one = password[position_one]
        char_two = password[position_two]

        valid_chars = 0

        # verify password policy
        if char_one == policy_char:
            valid_chars += 1
        if char_two == policy_char:
            valid_chars += 1

        if valid_chars == 1:
            valid_password_count += 1

    return valid_password_count


def main():

    password_data = get_password_data()
    # print(f"password_data is: {password_data}")

    number_of_valid_passwords = count_valid_passwords(password_data)
    print(f"number of valid passwords is: {number_of_valid_passwords}")

    number_of_actual_valid_passwords = count_actual_valid_passwords(password_data)
    print(f"number of actual valid passwords is: {number_of_actual_valid_passwords}")

    return

if __name__ == "__main__":
    main()
