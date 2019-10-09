def average(A):
	return int(sum(A) / len(A))

if __name__ == '__main__':
	  A = list(map(int, input().split()))
	  print(average(A))
