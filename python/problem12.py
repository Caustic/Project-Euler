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
            temp = factor(number/i)
            if not temp:
                factors.append(i)
                factors.append(number/i)
            else:
                factors.extend(temp)
            break
    return factors
