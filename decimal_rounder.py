#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Sat/May29/2021
# This program round the decimal to how many the user wants.


def decimal_rounder(decimal_number, round_number):
    # this function procces rounding the decimal number

    # process
    rounder = float(round(decimal_number, round_number))
    # return
    return rounder


def main():
    # this function this function call other functions

    # input
    decimal_str = input("Enter the number you want to round: ")
    round_str = input("Enter how many decimal places you want to round by: ")
    try:
        decimal_number = float(decimal_str)
        round_number = int(round_str)
        # call function
        decimal_rounder(decimal_number, round_number)
        # output
        print(
            "\nthe rounded number is {0}"
            .format(decimal_rounder(decimal_number, round_number)))
    except Exception:
        print("\nInvaild Input!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
