def max_even(A):
	B = A[:]
	for i in A:
		if i % 2 == 1:
			B.remove(i)
	if len(B) == 0:
		return None
	else:
		return max(B)


if __name__ == '__main__':
	A = list(map(int, input().split()))
	print(max_even(A))

