students=[];
n=int(raw_input())
if ( n>=2 and n<=5):   
    for i in range(n):
        name = raw_input()
        score = float(raw_input())
        
        students.append([score,name]);
else :
    print "looser"


#def takeSecond(elem):
 #   return elem[1]
students.sort()


if (students[0][0] < students[1][0] and students[1][0] != students[2][0]):
    print students[1][1]
elif (students[0][0] < students[1][0] and students[1][0]==students[2][0]):
    print students[1][1]    
    print students[2][1]
elif (students[0][0]==students[1][0] and students[1][0] < students[2][0] and students[2][0] !=students[3][0]) :
    print students[2][1]
elif (students[0][0]==students[1][0] and students[1][0] < students[2][0] and students[2][0]==students[3][0]) :
    print students[2][1]  
    print students[3][1]
elif (students[0][0]==students[1][0] and students[1][0] == students[2][0]) :
    print students[3][1]
     
