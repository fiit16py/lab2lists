def cut_swap(A,n):
    F=A.copy()
    nu=0
    for i in range(n,len(A)):
        A[nu]=F[i]
        nu=nu+1
    for i in range(n):
        A[nu]=F[i]
        nu=nu+1
    print(list(A))

if __name__ == '__main__':
    A = list(map(int, input().split()))
    n = int(input())
    print(cut_swap(A,n))
