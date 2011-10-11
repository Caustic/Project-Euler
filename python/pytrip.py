#! /usr/bin/python2
import math

def answer(a,b):
	return (math.sqrt(a**2 + b**2) + a + b - 1000)

def main():
	for a in range(1,500):
		for b in range(1,500):
			if(answer(a,b) == 0):
				c = math.sqrt(a**2 + b**2)
				print 'a = {} b = {} c = {}'.format(a,b,c)
				return

main()

