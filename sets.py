

n=(raw_input())
k = map(int,raw_input().split())
print k
print set(k)
l = len(set(k))
print l 
o= sum(set(k))
print(o)

q=(o / float(l))
print q
