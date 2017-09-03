import textwrap
def wrapy():
    S=raw_input()
    w=int(raw_input())
    if (len(S) < 1000 and w < len(S)):
        print textwrap.fill(S,w)
    return();
wrapy()

    

        
