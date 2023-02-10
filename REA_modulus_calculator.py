#!/usr/bin/env python3
# This algorithm was derived from the explanation given in the Class4Crypt 
# lessons (2.5. Algoritmo de Exponenciación Rápida)
# This program calculates the modulus of a large 
# number b^e using the Rapid Exponentiation Algorith (REA) which
# leverages the exponentiation by squaring principle

# Written by Marc Pascual i Solé

def get_bit_by_index(e, i):
	# e: integer
	# i: index
	# The string bin(x) has the form 0bXXXX, so we need to skip the 1st 2 chars, hence the +2
	return int(bin(e)[i+2])

def square_method_loop(b: int,e: int,m: int):
	# Where b is the base, e is the exponent and m is the number that defines the group Z/mZ
	b_p = b
	e_p = e
	res = 1
	# We iterate through each bit of the exponent.
	for i in range(0,e_p.bit_length()):
		bit = get_bit_by_index(e_p, i)

		if (bit & 1 > 0):			# Square and multiply
			res = (res * res * b_p) % m

		else: 					# Square
			res = (res * res) % m
		print("[*] Step %d: x=%d"%(i,res))
	return res

def main():
	b = int(input("Base: "))
	e = int(input("Exponent: "))
	m = int(input("Modulus: "))
	result = square_method_loop(b,e,m)

	print("The result of (%d^%d)mod(%d) = %d"%(b,e,m,result))

if __name__ == '__main__':
	main()
