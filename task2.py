def max_even(A):
	A.sort(reverse=True)
	for i in A:
		if i % 2 == 0:
		    return i
	return "None"

if __name__ == '__main__':
	A = list(map(int, input().split()))
	print(max_even(A))
