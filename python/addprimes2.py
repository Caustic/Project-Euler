#! /usr/bin/python2

import isprime

total = 3 
for i in range(3,2000000):
	if(isprime.isprime(i)):
		total = total + i

print total
