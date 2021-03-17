def for_e():
    """printing small 'e' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==0 and row not in(0,6) or col==3 and row in(1,2)  or row==0 and col in(1,2) or row==3 and col in(1,2) or row==6 and col!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_e():
    """printing small 'e' using while loop"""
    i=0
    while i<5:
        j=0
        while j<4:
            if j==0 and i not in (0,4) or i==4 and j!=0 or i==0 and j in(1,2) or i==2and j!=3 or i==1 and j==3:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

