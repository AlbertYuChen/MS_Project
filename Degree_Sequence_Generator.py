#!/usr/bin/env python

from random import randint




def degree_sequence_generator( length , deg_low, deg_high):
	degree_sequence = []
	sum_deg = 0
	deg = 0

	for d in range(0, length):
		deg = randint(deg_low,deg_high)
		sum_deg += deg
		degree_sequence.append(deg)

	# print(degree_sequence)


	if sum(degree_sequence) % 2 != 0 :
		degree_sequence[0] += 1


	# print sum(degree_sequence)

	return degree_sequence


if __name__ == '__main__':

    functionname( 64 , 6, 10)


