def print_formatted(n):
    for i in range (1,n+1):
            print (("").center(n))+i+(("").center(n))+oct(i)[1:]+(("").center(n))+hex(i)[2:]+(("").center(n))+bin(i)[2:]
    return();
print_formatted(n=int(raw_input()))
