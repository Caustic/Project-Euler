#! /usr/bin/python2
# Problem 4 at Project Euler
# Finds the largest Palindrome less than 999**2
# which is the product of two 3 digit numbers

#check to see if number is palindrome
def ispalindrome(palinum):
	return str(palinum)[::-1] == str(palinum) 

def main():
#start range high because we're looking for the highest
	for i in range(998001, 0, -1):
		if ispalindrome(i):
			for j in range(999, 100, -1):
#if it's divisible
				if i%j==0:
					if(i/j < 999):
						print i," ",j
						return

main()
