n = 6

def factrec(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return n*factrec(n-1)

print(factrec(n))
