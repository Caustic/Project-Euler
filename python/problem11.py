#! /usr/bin/python2

import sys

def makestr(somefile):
    tempstring = somefile.readline()[:]
    if(tempstring == ""):
        return ""
    return tempstring + makestr(somefile)


f = open('matrix')
numstring = makestr(f)
#print(numstring)
numstring = numstring.replace('\n',' ')
#print(numstring)

array = []
for j in range(0,20):
    new = []
    index = j * 60 
    for i in range(0,20):
        number = int(numstring[index + 3*i:index + 3*i+2])
        new.append(number)
        #print(number)
    array.append(new) 

#for i in range(0,20):
#    for j in range(0,20):
#        print array[i][j],
#    print ''

maximum = int()
for x in range(0,20):
    for y in range(0,16):
        prod = array[x][y]
        for i in range(1,4):
            prod = prod * array[x][y+i]
        maximum = prod if prod > maximum else maximum
for x in range(0,16):
    for y in range(0,20):
        prod = array[x][y]
        for i in range(1,4):
            prod = prod * array[x+i][y]
        maximum = prod if prod > maximum else maximum
for x in range(0,16):
    for y in range(0,16):
        prod = array[x][y]
        for i in range(1,4):
            prod = prod * array[x+i][y+i]
        maximum = prod if prod > maximum else maximum
for x in range(4,20):
    for y in range(0,16):
        prod = array[x][y]
        for i in range(1,4):
            prod = prod * array[x-i][y+i]
        maximum = prod if prod > maximum else maximum
print(maximum)
