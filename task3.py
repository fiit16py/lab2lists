def cut_swap(A,n):
<<<<<<< HEAD
    if (n > len(A)):
        return -1
    for i in range(len(A) // 2):
        A[i], A[len(A) - 1 - i] = A[len(A) - 1 - i], A[i]
        #A[i], A[i + n] = A[i + n], A[i]
    for i in range((len(A) - n) // 2):
        A[i], A[len(A) - n - 1 - i] = A[len(A) - n - 1 - i], A[i]
    for i in range(n // 2):
        A[len(A) - i - 1], A[len(A) - n + i] = A[len(A) - n + i], A[len(A) - i - 1]
=======
    A[0] = A[n]

>>>>>>> master

if __name__ == '__main__':
    A = list(map(int, input().split()))
    dlina_pervogo_otrezka = int(input())
    cut_swap(A, dlina_pervogo_otrezka)
    print(A)
