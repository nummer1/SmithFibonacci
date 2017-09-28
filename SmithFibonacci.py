from math import sqrt
from functools import reduce
	

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


markers = int(100)
def fibonacci_and_smith(n):
	l = [1,1]
	r = []
	for i in range(n):
		next = l[-1] + l[-2]
		if i%markers == 0:
			print("Marker: ", i, next)
		l.append(next)
		if is_smith_number(next):
			print("!!!", next)
			r.append(next)
	return r


fibonacci_and_smith(int(1e12))