def max_even(A):
	j=0
	max=A[0]
	for i in A:
		if j==1:
			max=A[1]
		if (j+1)%2==0:
			if max<A[j]:
				max=A[j]
		j+=1
	if j>1:
		return max
	else:
		return None
if __name__ == '__main__':
	  A = list(map(int, input().split()))
	  print(max_even(A))
