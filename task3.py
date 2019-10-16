def cut_swap(A,n):
    inf=0
    for i in range (n//2):
        A[n-i-1],A[i]=A[i],A[n-i-1]
    print(A)
    for i in range((len(A)-n)//2):
        A[n+i],A[-i-1]=A[-i-1],A[n+i]
    for i in range(len(A)//2):
        A[i],A[-i-1]=A[-i-1],A[i]
    print(A)

if __name__ == '__main__':
    A = list(map(int, input().split()))
    n = int(input())
    print(cut_swap(A,n))
