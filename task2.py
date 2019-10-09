def max_even(A):
    m = A[:]
    for i in A:
        if i % 2 == 1:
            m.remove(i)
    if len(m) == 0:
        return None
    else:
        return max(m)

if __name__ == '__main__':
    A = list(map(int, input().split()))
    print(max_even(A))
