import math
from copy import copy

LIMIT = 1000000

def IsPrime(number):
	if (number == 2):
		return True
		
	for i in range(2, int(math.ceil(math.sqrt(number))) + 1):
		if (number % i == 0):
			return False

	return True
	
def CreatePrimesList():
	list = []
	for i in range(2, LIMIT):
		if (IsPrime(i)):
			list.append(i)
			
	return list
	
def FindLongestSumPrime():
	primes_list = CreatePrimesList()

	longest_terms_list_length = 0
	longest_sum = 0
		
	for i in primes_list:		
		current_terms_list_length = 1
		current_sum = i
			
		for j in primes_list:
			if (j <= i):
				continue

			current_sum += j
			current_terms_list_length += 1
				
			if (current_sum >= LIMIT):
				break
						
			if (IsPrime(current_sum)):
				if (current_terms_list_length > longest_terms_list_length):
					longest_terms_list_length = current_terms_list_length
					longest_sum = current_sum
					
	print longest_terms_list_length			
	return longest_sum
			
print FindLongestSumPrime()