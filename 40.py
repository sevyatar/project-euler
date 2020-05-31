import math

INDEXES_TO_MULTIPLY = [1, 10, 100, 1000, 10000, 100000, 1000000]
#INDEXES_TO_MULTIPLY = [1, 10, 100, 1000, 10000, 100000]
#INDEXES_TO_MULTIPLY = [1, 10, 100]

def CreateDigitsString():
	global digits_string
	
	string_list = list("0" * INDEXES_TO_MULTIPLY[len(INDEXES_TO_MULTIPLY) - 1])
	current_index = 0
	i = 1
	while (current_index < len(string_list)):
		new_string = str(i)
		for ch in new_string:
			if (current_index >= len(string_list)):
				break
				
			string_list[current_index] = ch
			current_index += 1
			
		i += 1
		
	digits_string = "".join(string_list)
		

def Calculate():
	global digits_string
	CreateDigitsString()
	
	product = 1
	for i in INDEXES_TO_MULTIPLY:
		product *= int(digits_string[i - 1])
		
	return product
			
print Calculate()