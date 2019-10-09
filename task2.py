def max_even(A):
	arr = [b for b in A if b%2 ==0]
	if len(arr) == 0:
		return None
	else:
		return max(arr)

if __name__ == '__main__':
	  A = list(map(int, input().split()))
	  print(max_even(A))
