import math

NUMBER = 600851475143
#NUMBER = 13195
#NUMBER = 10

def FindBiggestDivider(number):
	current_number = number
	biggest_divider = 0
	
	while True:
		i = 2 
		while (i < int(math.ceil(current_number / 2)) + 1):
			if (current_number % i == 0):
				biggest_divider = max(biggest_divider, i)
				current_number = current_number / i
				break
			i += 1
			
		if (i == int(math.ceil(current_number / 2)) + 1):
			biggest_divider = max(biggest_divider, current_number)
			break
			
	return biggest_divider
	
print "Biggest Divider: " + str(FindBiggestDivider(NUMBER))
