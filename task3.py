def cut_swap(A,n):
	N = len(A)
	for i in range(N//2):
		A[i], A[N-1-i] = A[N-1-i], A[i]
	for i in range((N-n)//2):
		A[i], A[N-n-1-i] = A[N-n-1-i], A[i]
	for i in range(n//2):
		A[N-n-i], A[N-1-i] = A[N-1-i], A[N-n-i]


if __name__ == '__main__':
    A = list(map(int, input().split()))
    dlina_pervogo_otrezka = int(input())
    cut_swap(A, dlina_pervogo_otrezka)
    print(A)
