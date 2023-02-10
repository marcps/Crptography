#!/usr/bin/env python3
# This program calculates the modulus of a large 
# number b^e using the so called schneier loop which
# leverages the exponentiation by squaring principle

# Written by Marc Pascual i Solé

def schneier_loop(b: int,e: int,m: int):
	# Where b is the base, e is the exponent and m is the number that defines the group Z/mZ
	b_p = b
	e_p = e
	res = 1
	while(e_p > 0):
		if (e_p & 1 > 0):
			res = (b_p * res) % m
		print(res)
		b_p *= b_p
		e_p = e_p >> 1
	return res

def main():
	b = int(input("Base: "))
	e = int(input("Exponent: "))
	m = int(input("Modulus: "))
	result = schneier_loop(b,e,m)

	print("The result of (%d^%d)mod(%d) = %d"%(b,e,m,result))

if __name__ == '__main__':
	main()
