import AoC_tools as AT
import argparse


def balance_expense_report_2(report):
    done = False
    product = 1

    # get first number
    for ind1, num1 in enumerate(report):
        if not isinstance(num1, int):
            num1 = int(num1)
        # get second number
        for ind2, num2 in enumerate(report[ind1+1:]):
            if not isinstance(num2, int):
                num2 = int(num2)
            # check sum
            if num1 + num2 == 2020:
                done = True
                # print product
                product = num1 * num2
                break
        if done:
            break
    return product


def balance_expense_report_3(report):
    done = False
    product = 1

    # get first number
    for ind1, num1 in enumerate(report):
        if not isinstance(num1, int):
            num1 = int(num1)
        # get second number
        for ind2, num2 in enumerate(report[ind1+1:]):
            if not isinstance(num2, int):
                num2 = int(num2)
            # get third number
            for ind3, num3 in enumerate(report[ind2+1:]):
                if not isinstance(num3, int):
                    num3 = int(num3)
                # check sum
                if num1 + num2 + num3 == 2020:
                    done = True
                    product = num1 * num2 * num3
                    break
                if done:
                    break
            if done:
                break
        if done:
            break
    return product


def part_one(input_data):
    res = balance_expense_report_2(input_data)
    print("\nproduct: ", res)


def part_two(input_data):
    res = balance_expense_report_3(input_data)
    print("\nproduct: ", res)


def both(input_data):
    res = balance_expense_report_2(input_data)
    print("\nproduct: ", res)
    res = balance_expense_report_3(input_data)
    print("product: ", res)


if __name__ == '__main__':
    report = AT.load_txt(input("please enter data path: \n"))

    res = balance_expense_report_2(report)
    print("\npart one product: ", res)
    res = balance_expense_report_3(report)
    print("part two product: ", res)
