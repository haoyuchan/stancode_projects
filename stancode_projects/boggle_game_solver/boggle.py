"""
File: boggle.py
Name: Johnny Chan
----------------------------------------
This program will find all anagrams in the
boggle board that the user input.

example:
boggle board =[
	['f', 'y', 'c', 'l'],
	['i', 'o', 'm', 'g'],
	['o', 'r', 'i', 'l'],
	['h', 'j', 'h', 'u']
]

If you correctly implement this program, you should see all the words in the boggle board below:
Found firm
Found form
Found foil
.....
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
SIZE = 4


def main():
	"""
	1. Get the letter that the user input
	2. Check the illegal input format (every letter should have space between: 'a'' ''f'' ''t'' ''r')
	3. Remove the string with space and append in boggle board list
	4. Find the word in boggle board
	"""
	start = time.time()
	####################
	boggle_board = []
	while len(boggle_board) < SIZE:
		row = input(f"{len(boggle_board)} row of letters: ").lower().split()  # Get the letter that the user input (string)
		if len(row) == SIZE:
			check = True
			for i in row:
				if len(i) != 1 or not i.isalpha():
					print('illegal input')
					check = False
					break
			if check:
				boggle_board.append(row)
		else:
			print('illegal input')
	find_anagrams(boggle_board)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_anagrams(boggle_board):
	"""
	:param boggle_board: The 4x4 letter board.
	-------------------------------
	Find anagrams word in the Boggle board
	print the number of words in the boggle board
	"""
	dict_words = read_dictionary()
	ans_lst = []
	for x in range(SIZE):
		for y in range(SIZE):
			start_index = (x, y)
			current_s = boggle_board[x][y]
			used_index = [start_index]
			find_anagrams_helper(boggle_board, dict_words, current_s, start_index, used_index, ans_lst)

	print(f"There are {len(ans_lst)} words in total.")


def find_anagrams_helper(boggle_board, dict_words, current_s, start_index, used_index, ans_lst):
	"""
	:param boggle_board:The 4x4 letter board.
	:param dict_words: The list of words in the dictionary.
	:param current_s: The current string being formed.
	:param start_index: The starting index for the current string.
	:param used_index: The list of used indices.
	:param ans_lst: The list of found anagrams.
	"""
	# base case
	if len(current_s) >= SIZE and current_s in dict_words and current_s not in ans_lst:
		ans_lst.append(current_s)
		print(f"Found {current_s}")
		# to find the longest ans
		find_anagrams_helper(boggle_board, dict_words, current_s, start_index, used_index, ans_lst)
	else:
		# Loop over the neighbors and itself.
		for i in range(-1, 2, 1):
			for j in range(-1, 2, 1):
				new_x = start_index[0]+i
				new_y = start_index[1]+j
				if 0 <= new_x < SIZE and 0 <= new_y < SIZE:
					if (new_x, new_y) not in used_index:
						# choose
						current_s += boggle_board[new_x][new_y]
						start_index = (new_x, new_y)
						used_index.append(start_index)
						# explore
						if has_prefix(current_s, dict_words):
							find_anagrams_helper(boggle_board, dict_words, current_s, start_index, used_index, ans_lst)
						# un-choose
						current_s = current_s[:-1]
						start_index = (new_x-i, new_y-j)
						used_index.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	lst = []
	with open(FILE, 'r') as f:
		for line in f:
			lst.append(line.strip())
		words_set = set(lst)
	return words_set


def has_prefix(sub_s, dict_words):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dict_words: (list) a list of words in the dicitonary
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict_words:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
