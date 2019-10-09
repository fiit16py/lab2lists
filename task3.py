def cut_swap(A,n):
    #A[0] = A[n]
    a = A.copy()
    for i in range(n):
    	A.remove(a[i])
    for i in range(n):
    	A.append(a[i])
    return A

if __name__ == '__main__':
    A = list(map(int, input().split()))
    dlina_pervogo_otrezka = int(input())
    cut_swap(A, dlina_pervogo_otrezka)
    print(A)
