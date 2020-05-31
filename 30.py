import math

POWER = 5

SEARCH_MIN = 2
SEARCH_MAX = (9 ** POWER) * 10

def GetDigitPowerSum(number):
	number_string = str(number)
	sum = 0
	for ch in number_string:
		sum += int(ch) ** POWER
		
	return sum
	
def CheckNumber(number):
	power_sum = GetDigitPowerSum(number)
	
	if (number > power_sum):
		return 1
	elif (number < power_sum):
		return -1
	else:
		return 0
	
def FindSum():
	sum = 0

	for i in range(SEARCH_MIN, SEARCH_MAX):
		if (CheckNumber(i) == 0):
			sum += i
			
	return sum
		
print FindSum()