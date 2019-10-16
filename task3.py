def cut_swap(A,k):
    #return A[n:] + A[:n]
    n = len(A)
    for i in range(n // 2):
        A[i], A[n-1-i] = A[n-1-i], A[i]
    for i in range((n-k)//2):
        A[i], A[k-1-i] = A[k-1-i], A[i]
    for i in range(-1,(k-n)//2,-1):
        A[i], A[k-1-i] = A[k-1-i], A[i]


if __name__ == '__main__':
    A = list(map(int, input().split()))
    dlina_pervogo_otrezka = int(input())
    cut_swap(A, dlina_pervogo_otrezka)
    print(A)
