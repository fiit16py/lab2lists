def average(A):
    count = 0
    for element in A:
        count += element
    return count / len(A)

if __name__ == '__main__':
	  A = list(map(int, input().split()))
	  print(average(A))
