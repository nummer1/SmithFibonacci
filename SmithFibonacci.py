from math import sqrt
from math import ceil
from functools import reduce
import pickle

	
try:
	file = open("fibonacci.txt", "r")
	fibo = []
	for line in file.readlines():
		fibo.append(int(line))
except FileNotFoundError:
	fibo = [1,1]


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
			
 
def is_smith_number(n):
	fac = factors(n)
	if len(fac) > 1:
		return sum_digits(n) == add_all_digits(fac)
	else:
		return False


def fibonacci_and_smith(n):
	r = []
	for i in range(n):
		next = fibo[-1] + fibo[-2]
		print("Marker: ", i)
		fibo.append(next)
		if is_smith_number(next):
			print("!!!", next)
			r.append(next)
	return r


def write_files():
	file = open("fibonacci.txt", "w")
	for numbers in fibo:
		file.write(number)


try:
	fibonacci_and_smith(int(1e12))
except KeyboardInterrupt:
	print("KeyBoardInterrupt")
finally:
	write_files()