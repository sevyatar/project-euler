import math

DIVISORS = range(1,20)

def CheckNumber(number):
	for divisor in DIVISORS:
		if (number % divisor != 0):
			return False
			
	return True

# must be even, must end with 0
def FindNumber():
	i = 20
	while True:
		if (CheckNumber(i)):
			return i
			
		i += 20

print FindNumber()