def cut_swap(A,n):
 
    a = len(A)
    for i in range (a//2):
        A[i], A[a-1-i]=A[a-1-i],A[i]
    
    for i in range ((n)//2):
        A[a-n+i], A[a-1-i]=A[a-1-i],A[a-n+i]
    print(A) 
    for i in range ((a-n)//2):
        A[i], A[a-n-1-i]=A[a-n-1-i],A[i]
        print(A)

if __name__ == '__main__':
    A = list(map(int, input().split()))
    dlina_pervogo_otrezka = int(input())
    cut_swap(A, dlina_pervogo_otrezka)
    print(A)
#1 2 3 4 5 6 7 8 9 10
#10
#2
#8