def max_even(A):
    return max([b for b in A if b % 2 == 0])

if __name__ == '__main__':
	  A = list(map(int, input().split()))
	  print(max_even(A))
