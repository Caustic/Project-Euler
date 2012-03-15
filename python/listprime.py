#! /usr/bin/python2
import math

#this function produces primes up to a top limit
# using a Seive of Eratosthenes
# taken from http://code.activestate.com/recipes/117119-sieve-of-eratosthenes/
# David Eppstein, UC Irvine, 28 Feb 2002
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

