n=int(raw_input())
k=map(int,raw_input().split())
ko=set(k)
print  set(k)
m=int(raw_input())
p=map(int,raw_input().split())
po=set(p)
s=ko.difference(po)
print set(s)
d= po.difference(ko)
print set(d)
q=','.join(str(x) for x in sorted(s))
z =','.join(str(x) for x in sorted(d ))
print q
print z

