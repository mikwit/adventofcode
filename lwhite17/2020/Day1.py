def balance_expense_report_2(report):
    done = False

    # get first number
    for ind1, num1 in enumerate(report):
        # get second number
        for ind2, num2 in enumerate(report[ind1+1:]):
            # check sum
            if num1 + num2 == 2020:
                done = True
                # print product
                print(num1 * num2)
                break
        if done:
            break


def balance_expense_report_3(report):
    done = False

    # get first number
    for ind1, num1 in enumerate(report):
        # get second number
        for ind2, num2 in enumerate(report[ind1+1:]):
            # get third number
            for ind3, num3 in enumerate(report[ind2+1:]):
                # check sum
                if num1 + num2 + num3 == 2020:
                    done = True
                    # print product
                    print(num1 * num2 * num3)
                    break
        if done:
            break


if __name__ == '__main__':
    with open('data1.txt', 'r') as f:
        reports = f.read().split('\n')

    # balance_expense_report_2(reports)
    balance_expense_report_3(reports)

