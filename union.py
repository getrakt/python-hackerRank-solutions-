n=int(raw_input())
s=map(int,raw_input().split())
p=set(s)
b=int(raw_input())
a=map(int,raw_input().split())
x=set(a)

print p.union(set(a))
