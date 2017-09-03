from itertools import groupby
c,k=raw_input().split()
for c ,k in groupby(int(c)):
                    
    print(len(list(c)), int(k)) 
