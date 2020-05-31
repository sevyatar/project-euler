import math

MIN_SEARCH_NUMBER = 900
MAX_NUMBER = 1000

#BASE_NUMBER = 99
#MIN_SEARCH_NUMBER = 10
#MAX_NUMBER = 100

def IsPalindrome(number):
	string_number = str(number)
	length = len(string_number)
	for i in range(length):
		if (string_number[i] != string_number[length - i - 1]):
			return False
			
	return True

def Run():
	max_palindrome = 0
	number1 = MIN_SEARCH_NUMBER
	while (number1 < MAX_NUMBER):
		number2 = number1
		while (number2 < MAX_NUMBER):
			multiple = number1 * number2
			#print multiple
			if (IsPalindrome(multiple)):
				max_palindrome = max(max_palindrome, multiple)
			number2 += 1
			
		number1 += 1
	
	print max_palindrome

	
	
Run()