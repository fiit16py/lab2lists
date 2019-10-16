def cut_swap(A,n):
    for i in range(n):
        A[n+i],A[i]=A[i],A[n+i]
    print(list(A))

if __name__ == '__main__':
    A = list(map(int, input().split()))
    n = int(input())
    print(cut_swap(A,n))

