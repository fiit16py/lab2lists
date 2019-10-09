def max_even(A):
	mx = 0
	for i in A:
		if i % 2 == 0:
			mx = max(mx, i)
	return mx

if __name__ == '__main__':
	A = list(map(int, input().split()))
	print(max_even(A))
