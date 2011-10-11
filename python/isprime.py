#! /usr/bin/python2
import math

def isprime(number):
	if (number % 2) == 0:
		return False
	for a in range(3, int(math.sqrt(number) + 1), 2):
		if (number % a) == 0:
			return False
	return True

