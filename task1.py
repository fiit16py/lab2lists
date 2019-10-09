def average(A):
    s = 0
    for x in A:
    	s += x
    s /= len(A)
    return s

if __name__ == '__main__':
	  A = list(map(int, input().split()))
	  print(average(A))