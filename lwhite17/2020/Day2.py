def parse_passwords_1(passwords):
    noValid = 0

    for pInd, password in enumerate(passwords):
        # find location of dash
        dashInd = password.find('-')
        if dashInd == -1:
            continue

        # find location of first space
        spaceInd = password.find(' ')
        if spaceInd == -1:
            continue

        # find minimum times character must be repeated
        minTimes = int(password[:dashInd])
        # find maximum times character must be repeated
        maxTimes = int(password[dashInd+1:spaceInd])

        # find location of colon
        colonInd = password.find(':')

        # find target character
        char = password[spaceInd+1:colonInd]

        # extract actual password
        password = password[colonInd+2:]

        # count appearances of target character
        times = password.count(char)

        # check threshold
        if minTimes <= times <= maxTimes:
            noValid += 1

    print(noValid)


def parse_passwords_2(passwords):
    noValid = 0

    for pInd, password in enumerate(passwords):
        # find location of dash
        dashInd = password.find('-')
        if dashInd == -1:
            continue

        # find location of first space
        spaceInd = password.find(' ')
        if spaceInd == -1:
            continue

        # find potential positions of target character
        pos1 = int(password[:dashInd])
        pos2 = int(password[dashInd+1:spaceInd])

        # find location of colon
        colonInd = password.find(':')

        # find target character
        char = password[spaceInd+1:colonInd]

        # extract actual password
        password = password[colonInd+2:]

        isPos1 = (password[pos1 - 1] == char)
        isPos2 = (password[pos2 - 1] == char)

        # check only one position contains target character
        if isPos1 and isPos2:
            continue
        if isPos1 or isPos2:
            noValid += 1

    print(noValid)


if __name__ == '__main__':
    with open('data2.txt', 'r') as f:
        passwords = f.read().split('\n')

    # parse_passwords_1(passwords)
    parse_passwords_2(passwords)
