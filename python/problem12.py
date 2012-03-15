#! /usr/bin/python2

#problem 12 project euler
from listprime import listprimes
from math import sqrt

def factor(number):
    print(number)
    factors = list([])
    for i in listprimes(sqrt(number)):
        if (number % i == 0):
            factors.append(i)
            factors.extend(factor(number/i))
            break
    return factors
