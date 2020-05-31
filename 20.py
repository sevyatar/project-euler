import math

FACTORIAL = 100

def GetDigitSum(number):
	number_string = str(number)
	sum = 0
	for ch in number_string:
		sum += int(ch)
		
	return sum
	
def CalcFactorial():
	factorial = 1
	for i in range(1, FACTORIAL):
		factorial *= i
		
	return factorial
	
	
print GetDigitSum(CalcFactorial())