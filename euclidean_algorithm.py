#!/usr/bin/env python
# This program calculates the gcd(a,b) using the 
# Euclidean Algorithm with the property: 
# gcd(a,b) = gcd(b,r) where a=qb+r; r is the remainder

# Written by Marc Pascual i Solé
import sys

def banner():
	print("GCD calculator. This program calculates the gcd(a,b) of two integers a and b")

def usage():
	banner()
	print("[?] Usage: %s <a> <b>"%sys.argv[0])
	sys.exit()

def print_result(s,a,b):
	print("\n[*] gcd(%s, %s) = %s\n"%(a,b,s))

def eclidean_aglorithm(a,b):
	if a<b:
		bp=b;b=a;a=bp # if a<b then change them

	r = a%b
	while(r!=0):
		a=b
		b=r
		r=a%b
	return b

def main():
	if len(sys.argv)<3:
		usage()
	banner()
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	print_result(eclidean_aglorithm(a, b),a,b)


if __name__ == '__main__':
	main()
