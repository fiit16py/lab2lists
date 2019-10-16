def max_even(A):
	while A:
		if max(A)%2==0:
			return max(A)
		else:
			A.remove(max(A))
	return False

if __name__ == '__main__':
	  A = list(map(int, input().split()))
	  print(max_even(A))
