#! /usr/bin/python2

import listprime

total = 2
for i in listprime.listprimes(2000000):
	total += i

print total
