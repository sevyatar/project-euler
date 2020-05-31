LIMIT = 4000000

sum = 0
prev = 1
current = 2

while current < LIMIT:		
	if (current % 2 == 0):
		sum += current
		
	new_current = prev + current
	prev = current	
	current = new_current
			
print sum