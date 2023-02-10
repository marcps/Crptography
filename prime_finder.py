#!/us/bin/python3
import math

def is_prime(p : int):
	for i in range(0,p):
		if (p % i == 0):
			return False
	return True

# -------------------------------------------------------------
# The following function has been extracted from:
# https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
# -------------------------------------------------------------
# A function to print all prime factors of
# a given number n
def primeFactors(n):
	plist = list()
    # Print the number of two's that divide n
	while n % 2 == 0:
		plist.append(2)
		n = n / 2  
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
	for i in range(3,int(math.sqrt(n))+1,2):
        # while i divides n , print i and divide n
		while n % i== 0:
			plist.append(int(n)),
			n = n / i           
    # Condition if n is a prime
    # number greater than 2
	if n > 2:
		plist.append(int(n))
	return plist
# -------------------------------------------------------------
def root_condition(p : int, a : int, l : list):
	for qi in l:
		if a**((p-1)/qi)%p == 1:
			return False
	return True

def prime_root_method(p : int):
	# First, we need to find all prime factors of p-1
	prime_factors = primeFactors(p-1)
	print(prime_factors)
	# We will now remove all duplicates from the list
	plist = [*set(prime_factors)]

	root_list = list()

	for i in range(1,p):
		if root_condition(p, i, plist):
			root_list.append(i)

	print(root_list)





def main():
	prime_root_method(13)


if __name__ == '__main__':
	main()