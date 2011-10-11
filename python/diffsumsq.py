#! /usr/bin/python2

def sums(number):
	if number == 0:
		return 0
	return number + sums(number-1)

def sumsq(number):
	if number == 0:
		return 0
	return number**2 + sumsq(number-1)

print sums(100)**2 - sumsq(100)
