"""
File: hangman.py
Name: Johnny Chan
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Pre-condition: Users see a dashed word, trying to correctly figure the un-dashed word out by inputting
    one character each round.
    Post-condition: showing the correct word in the console.
    """
    ans = random_word()  # choose the random word

    # replacing the word by print the dashes
    guess_ans = ""
    print("The word looks like ", end="")
    for i in range(len(ans)):
        guess_ans += "-"
    print(guess_ans)

    # the number of guess the player has.
    count = N_TURNS
    while True:
        print("You have " + str(count) + " wrong guess left.")
        # getting user input
        guess = input("Your guess: ").upper()

        # user input wrong format
        if not guess.isalpha() or len(guess) > 1:   # not a alphabet or more than one letter
            print("illegal format")
            guess = input("Your guess: ").upper()

        # alphabet in the answer
        if guess in ans:
            print("You are correct!")
            new_ans = replace(guess, ans, guess_ans)
            guess_ans = new_ans
            if guess_ans != ans:
                print("The word looks like ", end="")
                print(new_ans)
            else:
                print("You win!!")
                print("The word was: " + ans)
                break

        # alphabet not in the answer
        else:
            print("There is no " + str(guess)+"'s in the word.")
            count -= 1   # takes away a count if wrong

            # when count == 0 you lose
            if count == 0:
                print("You are completely hung : ( ")
                print("The word was: " + ans)
                break


def replace(guess, ans, guess_ans):
    """
    :param guess: str, letter user input
    :param ans: str, correct answer
    :param guess_ans: str, letter that user current guess
    :return: str
    """
    new_ans = ""
    for i in range(len(ans)):
        if guess == ans[i]:  # alphabet in the answer
            if i == 0:
                new_ans = guess + guess_ans[1:]         # alphabet at the first position
            elif i == len(ans):
                new_ans = guess_ans[:len(ans) - 1] + guess      # alphabet at the last position
            else:
                new_ans = guess_ans[:i] + guess + guess_ans[i + 1:]       # alphabet in the middle position
            guess_ans = new_ans
    return new_ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
