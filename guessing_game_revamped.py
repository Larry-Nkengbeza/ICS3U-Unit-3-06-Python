# 3/usr/bin/env Python3

# Created by Larry Nkengbeza
# Created in December 2020
# This program is a guessing game

import random


def main():
    # Input
    user_guess_str = input("Enter a random INTEGER (-10-9): ")
    computer_answer = random.randint(-10, 9)
    # Process and output

    try:
        # this might fail if they enter words
        user_guess = int(user_guess_str)

        if user_guess == computer_answer:
            print("Exactly right answer")
        else:
            print("Wrong number. The correct number is {0}"
                  .format(computer_answer))
    except Exception:
        print("This was not an integer.")
    finally:
        print("Thanks for playing.")


if __name__ == "__main__":
    main()
