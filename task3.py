def cut_swap(E, k):
    E = E[k:]+E[0:k]
    print(E)
if __name__ == '__main__':
    print("Введите A")
    A = list(map(int, input().split()))
    print("Введите n")
    n = int(input())
    cut_swap(A, n)
