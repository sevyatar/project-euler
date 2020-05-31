import math

REQUIRED_SUM = 1000
LARGEST_A_VALUE = int(math.ceil(REQUIRED_SUM / 3))
LARGEST_B_VALUE = int(math.ceil(REQUIRED_SUM / 2))

def IsTripletLegal(a, b, c):
	if (a + b + c != 1000):
		return False
		
	if ((a*a) + (b*b) != (c*c)):
		return False
		
	return True

def FindTriplet():
	for a in range(1, LARGEST_A_VALUE + 1):
		for b in range(a + 1, LARGEST_B_VALUE + 1):
			c = 1000 - a - b
			if (IsTripletLegal(a, b, c)):
				return ([a,b,c])
	
[a,b,c] = FindTriplet()
print a * b * c