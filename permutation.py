from itertools import permutations
n,k=(raw_input().split())
print n,k
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')
