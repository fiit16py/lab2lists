def cut_swap(A, n):
    for j in range(n):
        for i in range(len(A) - 1):
            A[i], A[i + 1] = A[i + 1], A[i]


if __name__ == '__main__':
    A = list(map(int, input().split()))
    n = int(input())
    cut_swap(A, n)
    print(A)
