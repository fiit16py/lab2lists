def average(A):
    s=0
    k=0
    for i in A:
        s+=i
        k+=1
    return s/k

if __name__ == '__main__':
	  A = list(map(int, input().split()))
	  print(average(A))
