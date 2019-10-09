def average(A):
    s = 0
    for i in A:
        s += i
    return s/len(A)

if __name__ == '__main__':
    A = list(map(int, input().split()))
    print(average(A))
