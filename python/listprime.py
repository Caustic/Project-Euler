#! /usr/bin/python2
import math

def listprimes(toplimit):
	D = {}
	q = 2
	while (q < toplimit):
		if q not in D:
			yield q
			D[q*q] = [q]
		else:
			for p in D[q]:
				D.setdefault(p+q,[]).append(p)
			del D[q]
		q += 1

