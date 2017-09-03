def mutant(n):
    i,e=(raw_input().split(" "))
    i=int(i)
    l=list(n)
    n= n[:i] + e + n[(i+1):]
    print n
    return;

mutant(n=raw_input());

