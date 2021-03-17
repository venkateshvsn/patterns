def for_j():
    """printing small 'j' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==3 and row!=6 or col==0 and row in(4,5) or row==6 and col in(1,2) :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_j():
    """printing small 'j' using while loop"""
    i=0
    while i<6:
        j=0
        while j<3:
            if j==2 and i not in (1,5) or i==5 and  j==1 or j==0 and i==4:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

