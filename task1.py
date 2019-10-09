def average(A):
    summ=0
    for i in range(len(A)):
        summ=summ+A[i]
    summ=summ/len(A)
    return summ

if __name__ == '__main__':
    A = list(map(int, input().split()))
    print(average(A))
