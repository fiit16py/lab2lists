def average(A):
	s=0
	j=0
	for i in A:
		s+=A[j]
		j+=1

if __name__ == '__main__':
	A = list(map(int, input().split()))
	print(average(A))
