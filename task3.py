def cut_swap(A, n):
    A = A[n:] + A[:n]
    return A


if __name__ == '__main__':
    A = list(map(int, input().split()))
    dlina_pervogo_otrezka = int(input())
    print(cut_swap(A, dlina_pervogo_otrezka))
