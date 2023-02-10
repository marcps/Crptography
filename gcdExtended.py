#!/usr/bin/env python3
# This program calculates the inv(a,n) using the 
# Extended Euclidean Algorithm where:
# [a * inv(a,n)] mod(n) = 1

# Written by Marc Pascual i Solé
import sys

def banner():
	print("Inverse calculator. This program calculates the inv(a,n) of a in the modulus of n")

def usage():
	banner()
	print("[?] Usage: %s <a> <b>"%sys.argv[0])
	sys.exit()

def print_result(s,a,b):
	print("\n[*] inv(%s, %s) = %s\n"%(a,b,s))

def gcdExtended(a, n):

	#Initial Conditions
	u1, v1, u2, v2 = 1, 0, 0, 1
	g1,g2 = n, a
	
	while (g2 != 0):
		y = g1//g2
		g3 = g1%g2
		u3 = u1 - u2*y
		v3 = v1 - v2*y
		
		# Reset the values

		g1 = g2
		g2 = g3
		u1, u2, v1, v2 = u2, u3, v2, v3
	if v1<0:
		v1 = v1 + n
	return v1

def main():
	if len(sys.argv)<3:
		usage()
	banner()
	a = int(sys.argv[1])
	n = int(sys.argv[2])
	if a>n:
		tmp=a
		a = n
		n = tmp
	print_result(gcdExtended(a, n),a,n)

if __name__ == '__main__':
	main()