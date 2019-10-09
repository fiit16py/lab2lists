def max_even(A):
    while(True):
        m = max(A)
        if m % 2 == 0:
            return m
        elif len(A) > 1:
            A.pop(A.index(m))
            continue
        else:
            return None

if __name__ == '__main__':
	  A = list(map(int, input().split()))
	  print(max_even(A))
