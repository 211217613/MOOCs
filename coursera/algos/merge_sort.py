#!/usr/bin/python3
import random 
import logging
import math
import unittest
"""
Write a random int to a file for sorting
read the file contents into a list. 
Call merge sort algo
NOTE: randint gives lots of duplicates
"""

logging.basicConfig(level = logging.INFO,
					filename='./merge.log',
					filemode='w',
					format='%(asctime)s - %(levelname)s - %(message)s' )

NUMBER = 10 * 10
def randomize():
	logging.info('randomizing data')
	with open('./rand_integers.txt', 'w+') as rand:
		for x in range(0, NUMBER):
			var = random.randint(0, NUMBER)
			rand.write(str(var) + '\n')

def read_file(l1):
	with open('./rand_integers.txt', 'r') as rand_fd:
		for line in rand_fd:
			l1.append(line.rstrip())

	logging.info('reading file {} and appending'.format(rand_fd))

def merge_sort(alist):
	logging.info("merging list")
	l_list = list()
	r_list = list()

	list_len = len(alist)
	mid = len(alist) // 2

	l_list = alist[ : mid ]
	r_list = alist[ mid: ]
	logging.info( 'l_list {}'.format(l_list) )
	logging.info( 'r_list {}'.format(r_list) )

	if len(alist) == 1:
		return alist

	else:
		# recursion: break down into single element lists
		mid = len(alist) // 2
		l_list = merge_sort( alist[:mid] )
		r_list = merge_sort( alist[mid:] )


		l_counter = 0
		r_counter = 0
		master_counter = 0
		while l_counter < len(l_list) and r_counter < len(r_list):
			if l_list[l_counter] < r_list[ r_counter ]:
				alist[ master_counter ] = l_list[ l_counter ]
				l_counter = l_counter + 1 
			else:
				alist[ master_counter ] = r_list[ r_counter ]
			master_counter = master_counter + 1

		while l_counter < len(l_list):
			alist[ master_counter ] = l_list[ l_counter ]
			l_counter = l_counter + 1
			master_counter = master_counter + 1


def main():
	logging.info('Start in main')
	l1 = ['90', '88', '21', '73', '17', '38', '78', '77', '91', '88', '45', '82', '79', '97', '53', '18', '93', '22', '73', '62', '9', '11', '65', '100', '35', '97', '93', '69', '43', '87', '36', '61', '44', '47', '8', '57', '7', '12', '23', '91', '56', '69', '79', '80', '68', '92', '71', '8', '14', '41']

	# randomize()
	# read_file(l1)
	merge_sort(l1)

if __name__ == '__main__':
	main()