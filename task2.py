def max_even(A):
    max=None
    for i in range(len(A)):
        if A[i]%2==0:
            if max==None:
                max=A[i]
            if A[i]>max:
                max=A[i]
    return max

if __name__ == '__main__':
    A = list(map(int, input().split()))
    print(max_even(A))
