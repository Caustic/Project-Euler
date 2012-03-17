#! /usr/bin/python2
from math import sqrt
import sys
from factor import factor

def triangle_itr(upperlimit):
    i = 1
    count = 0
    while( i <= upperlimit ):
        count = count + i
        i += 1
        yield count

def combinations(elements, n):
    if n == 0:
        yield []
    else:
        for i in xrange(len(elements)):
            for cc in combinations(elements[i+1:],n-1):
                yield [elements[i]] + cc

def calcfactors(p_factors):
    t_factors = []
    for i in range(1,len(p_factors)+1):
        for f in combinations(p_factors,i):
            product = 1
            for j in range(0,len(f)):
                product = product * f[j]
            t_factors.append(product)
    return t_factors

def trinum(n):
    return (n-1)*n/2

def divisors(number):
    factors = []
    for i in range(2,int(sqrt(number)+1)):
        if(number%i == 0):
            factors.append(i)
    factors.append(1)
    return factors

#for i in triangle_itr(50000):
#    factors = factor(i)
#    if(len(factors) > 9):
#        if(len(set(calcfactors(factors))) > 500):
#            print factors
#            break

for i in range(10000,20000):
    if(len(divisors(trinum(i)))>=250):
        print i
        break
