from itertools import combinations
s,i= raw_input().split()
for i in range(1,int(i)+1):
            
    for p in combinations(sorted(s),int(i)):
        
        print ''.join(p)
