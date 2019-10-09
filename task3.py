def cut_swap(A, n):
    tempList = A.copy()
    for i in range(n, len(A)):
        A[i] = tempList[i - n - 1]

    for i in range(n):
        A[i] = tempList[i + n]


if __name__ == '__main__':
    A = list(map(int, input().split()))
    n = int(input())
    cut_swap(A, n)
    print(A)
