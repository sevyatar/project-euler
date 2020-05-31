import math

LIMIT = 100

def FindSquareDifference():
	final_sum = 0
	for i in range(1, LIMIT + 1):
		for j in range(i+1, LIMIT + 1):
			final_sum += 2*i*j
			
	return final_sum

print FindSquareDifference()