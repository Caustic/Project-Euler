#! /usr/bin/python2

#simple factorization problem
from listprime import listprimes
from math import sqrt

#simple factorization algoritm that uses a prime
# seive to test all factors recursively up to 
# sqrt of the number
def factor(number):
    factors = list([])
    for i in listprimes(sqrt(number)+1):
        #print(number)
        if (number % i == 0):
            factors.append(i)
            factors.extend(factor(number/i))
            return factors
    if number != 1:
        factors.append(number)
    return factors
