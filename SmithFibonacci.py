from math import sqrt
from math import ceil
from functools import reduce
import pickle


try:
	file = open("fibonacci.txt", "r")
	factorization = []
	for line in file.readlines():
		factorization.append(list(map(int, line.strip("\n").split())))
except FileNotFoundError:
	print("Fatal Error, run FibonacciFactorization first")
	quit()


def factors(n):
	i = 2
	fac = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			fac.append(i)
	if n > 1:
		fac.append(n)
	return fac
 
 
def sum_digits(n):
   r = 0
   while n:
	   r, n = r + n % 10, n // 10
   return r
   

def add_all_digits(l):
	s = 0
	for e in l:
		s += sum_digits(e) if e >= 10 else e
	return s
			
 
def is_smith_number(n, i):
	fac = factorization[i]
	if len(fac) > 1:
		return sum_digits(n) == add_all_digits(fac)
	else:
		return False


def fibonacci_and_smith(n):
	fibo = [1,1]
	r = []
	for i in range(3, n):
		next = fibo[-1] + fibo[-2]
		fibo.append(next)
		if is_smith_number(next, i):
			print("!!!", next)
			r.append(next)
	return r


fibonacci_and_smith(int(1001))