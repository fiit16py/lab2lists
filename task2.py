def max_even(A):
    maxn=A[0]
    for i in A:
        if i%2==0:
            if maxn<i:
                maxn=i
    return maxn

if __name__ == '__main__':
	  A = list(map(int, input().split()))
	  print(max_even(A))
