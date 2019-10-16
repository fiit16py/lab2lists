def max_even(A):
    maxn=min()A
    for i in A:
        if i%2==0:
            if maxn<i:
                maxn=i
    if maxn==min(A):
        return "None"
    else: return maxn
if __name__== '__main__':
    A =list(map(int,input().split()))
    print(max_even(A))
