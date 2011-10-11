#! /usr/bin/python2

def ispalindrome(palinum):
	return str(palinum)[::-1] == str(palinum) 

def main():
	for i in range(998001, 0, -1):
		if ispalindrome(i):
			for j in range(999, 100, -1):
				if i%j==0:
					if(i/j < 999):
						print i," ",j
						return

main()
