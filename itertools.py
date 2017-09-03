from itertools import product
n=map(int,raw_input().split())
b=map(int,raw_input().split())
k=list(product(n,b))
k=[str(a) for a in k]
print (", ".join(k))
 
