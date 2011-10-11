#! /usr/bin/python2

import sys

def makestr(somefile):
	tempstring = somefile.readline()[:-2]
	if(tempstring == ""):
		return ""
	return makestr(somefile) + tempstring

def calcprod(mystring, index):
	if(index == 0):
		return 0
	nums = list(mystring[index-5:index])
	local_num = 1
	for i in nums:
		local_num = local_num * int(i)
	maxnum = calcprod(mystring, index-1)
	return local_num if local_num > maxnum else maxnum
#	if(local_num > maxnum):
#		return local_num
#	else:
#		return maxnum

f = open('testfile')
numstring = makestr(f)
print numstring

sys.setrecursionlimit(1001)
print calcprod(numstring, 999)

