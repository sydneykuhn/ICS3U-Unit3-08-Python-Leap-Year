#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Sep 2020
# This program tells you if a year is a leap year


def main():
    # this function determines the answer

    # input
    user_year_as_string = input("Please enter the year : ")

    # process & output
    try:
        user_year = int(user_year_as_string)
        if user_year % 4 == 0:
            if user_year % 100 == 0:
                if user_year % 400 == 0:
                    print("{0} is a leap year.".format(user_year))
                else:
                    print("{0} is not a leap year.".format(user_year))
            else:
                print("{0} is a leap year.".format(user_year))
        else:
            print("{0} is not a leap year.".format(user_year))
    except Exception:
        print("Invalid year entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
