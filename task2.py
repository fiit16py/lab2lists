def max_even(A):
	m = max(A)
	if m % 2 = 0:
		return m
	else:
		return None

if __name__ == '__main__':
	  A = list(map(int, input().split()))
	  print(max_even(A))
