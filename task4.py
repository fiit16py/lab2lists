import numpy as np 
def rank(A):
    rk = np.linalg.matrix_rank(A)
    return rk

if __name__=='__main__':
    print('Enter matrix, enter single Q to finish')
    A = []
    line = input()
    while line not in ['Q', 'q']:
        A.append(list(map(float, line.split())))
        line = input()
    print('Ранг матрицы A равен', rank(A))
