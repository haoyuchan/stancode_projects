"""
File: anagram.py
Name: Johnny Chan
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    find all anagrams in the dictionary
    """
    start = time.time()
    ####################
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        string = input("Find anagrams for: ")
        if string != EXIT:
            find_anagrams(string)
        else:
            break
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    :return all_word: lst, all word in the dictionary
    """
    with open(FILE, "r")as f:
        all_word = [line.strip() for line in f]
        return all_word


def find_anagrams(s):
    """
    this function will find all anagrams in the dictionary and print the list
    :param s: string
    """
    all_word = read_dictionary()
    print('Searching...')
    ans_lst = []
    find_anagrams_helper(s, "", ans_lst, all_word)

    print(f'{len(ans_lst)} anagram: {ans_lst}')


def find_anagrams_helper(s, current_s, ans_lst, all_word):
    if len(s) == 0:  # base case
        if current_s in all_word and current_s not in ans_lst:
            ans_lst.append(current_s)
            print(f"Found: {current_s}")
            print("Searching...")
    else:
        for i in range(len(s)):
            # choose
            current_s += s[i]
            unused_s = s[0:i] + s[i+1:]
            # explore
            if has_prefix(current_s, all_word):
                find_anagrams_helper(unused_s, current_s, ans_lst, all_word)
            # un-choose
            current_s = current_s[:-1]


def has_prefix(sub_s, all_word):
    """
    :param sub_s: string
    :param all_word: lst
    :return: boolean
    """
    for word in all_word:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
