n = 6

temp1 = 1

while n != 1 and n != 0:
	temp2 = n * (n-1)
	temp1 = temp1 * temp2
	n -= 2

print(temp1)
