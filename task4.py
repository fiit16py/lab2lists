def rank(A):
    #down
    count = len(A)
    s = min([len(A), len(A[0])])
    for i in range(s - 1):
        for j in range(i + 1,len(A)):
            if A[i][i] == 0:
                continue
            d = A[j][i] / A[i][i]
            for k in range(i, len(A[0])):
                A[j][k] = A[j][k] - A[i][k] * d
    
    for i in range(len(A)):
        t = min(A[i])
        if t == max(A[i]) and t == 0:
            count -= 1
    return count

if __name__=='__main__':
    print('Enter matrix, enter single Q to finish')
    A = []
    line = input()
    while line not in ['Q', 'q']:
        A.append(list(map(float, line.split())))
        line = input()
    print('Ранг матрицы A равен', rank(A))
