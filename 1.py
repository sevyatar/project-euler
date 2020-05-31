LIMIT = 1000
MULTIPLE_1 = 3
MULTIPLE_2 = 5

sum = 0
for i in range(LIMIT):
	if (i % MULTIPLE_1 == 0 or i % MULTIPLE_2 == 0):
		sum += i
		
print sum