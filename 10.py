import math

LIMIT = 2000000

def IsPrime(number):
	if (number == 2):
		return True
		
	for i in range(2, int(math.ceil(math.sqrt(number))) + 1):
		if (number % i == 0):
			return False

	return True
	
def CalculateSum():
	sum = 0
	for i in range(2, LIMIT):
		if (IsPrime(i)):
			sum += i
			
	return sum
	
print CalculateSum()