def max_even(A):
    me = None
    for a in A:
        if a%2==0 and (me is None or a>me):  
            me = a
    return me

if __name__ == '__main__':
      A = list(map(int, input().split()))
      print(max_even(A))
