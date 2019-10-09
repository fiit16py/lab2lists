def average(A):
   sum=0:
   for i in A:
   	sum += i
   return sum/len(A) 

if __name__ == '__main__':
	  A = list(map(int, input().split()))
	  print(average(A))  
