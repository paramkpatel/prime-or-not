##########################################################################
#   Author:  Param Patel (parampatel@email.arizona.edu)
#   Class:  CSC 245, Spring 2022
#       SL:  N/A
#
#   Program:  Homework 6 and FToA
#   Due Date:  April 9th, 2022 @ 3:00pm
#
# Language:  Python 3
#   To Run:  $ python3 hmwk6.py
#
# Purpose: This program is demonstrating the Fundamental Theorem of
# Arithmetic of a number given on cmd line.
#
#  "Bugs": I don't know :) You'd have to tell me LOL
##########################################################################


import sys


def space_helper(space):
    """
    Space helper if just to get proper spacing for the print statements.
    :param: space: this is for spacing when the output is printed.
    :return: space
    """
    print("\t" * space, end="")
    return space


def is_prime(value, space):
    """
    This function first checks if the number is prime. Depending on
    the value if it's prime or not it will print out useful information
    and why the given number is not prime! Else it will print that
    the {value} is prime.
    :param: value: number the user gives in command-line
    :param: space: this is for spacing when the output is printed.
    :return: return
    """
    # negative number
    if value < 0:
        print("Negative integers can not be prime.")
    # if the value is prime
    for num in range(2, value):
        if value % num == 0:
            # if not prints info for why not
            if num != int(value / num):
                space_helper(space)
                print(f"{value} = {int(value / num)} * {num}; are these "
                      f"factors either prime or product of primes?")
                # recursive call and adds one space
                is_prime(int(value / num), space + 1)
                is_prime(num, space + 1)
                space_helper(space)  # spacing
                print(
                    f"{value} is the product of primes ({int(value / num)} and "
                    f"{num} are prime or prime products).")
            # if it is prints information why it is!
            else:
                space_helper(space)  # for proper spacing
                print(f"{value} = {int(value / num)} squared; is this "
                      f"factor either prime or product of primes?")

                is_prime(int(value / num), space + 1)
                space_helper(space)
                print(f"{value} is the square of {int(value / num)} "
                      f"which is prime or the product of primes.")
            return
        else:
            space_helper(space)
            # if value is prime prints that it is
            print(f"{value} is prime.")
            print()
            print(f"As this output shows, the Fundamental Theorem of "
                  f"Arithmetic holds for {sys.argv[1]}.")
            return


def main():
    if len(sys.argv) > 1:
        print(f"This program will demonstrate that {sys.argv[1]} is "
              f"either prime\nor is the product of two or more prime numbers.")
        print()
        is_prime(int(sys.argv[1]), 0)


if __name__ == "__main__":
    main()
