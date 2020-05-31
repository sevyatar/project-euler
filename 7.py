import math

PRIME_INDEX = 10001

def IsDividable(number, divisors):
	for i in divisors:
		if (number % i == 0):
			return True
			
	return False

def FindPrime(index):
	primes_list = [2]
	current_number = 3
	
	while (len(primes_list) < index):
		if (not IsDividable(current_number, primes_list)):
			primes_list.append(current_number)
		
		current_number += 2
		
	return primes_list[len(primes_list) - 1]
	
print FindPrime(PRIME_INDEX)