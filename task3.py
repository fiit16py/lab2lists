def cut_swap(A,n):
    for i in range(n):
        A    for i in range(n):
        A[i], A[len(A) - n + i] = A[len(A) - n + i], A[i]
        if len(A) / 2 != n:
            A[i], A[i + n] = A[i + n], A[i]

if __name__ == '__main__':
    A = list(map(int, input().split()))
    dlina_pervogo_otrezka = int(input())
    cut_swap(A, dlina_pervogo_otrezka)
    print(A)
