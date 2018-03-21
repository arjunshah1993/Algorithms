n = 6

def factwhile(n):
	temp1 = 1	
	while n != 1 and n != 0:
		temp2 = n * (n-1)
		temp1 = temp1 * temp2
		n -= 2
	return(print(temp1)

factwhile(n)
