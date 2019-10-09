def average(A):
	s=0
	j=0
	for i in A:
		# камент
		s+=A[j]
		j+=1
	s/=j
	return s
if __name__ == '__main__':
	A = list(map(int, input().split()))
	print(average(A))
