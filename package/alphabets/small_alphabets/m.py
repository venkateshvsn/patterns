def for_m():
    """printing small 'm' using for loop"""
    for row in range(6):
        for col in range(7):
            if col==0  or row==1 and col not in(0,3,6) or col==3 and row not in(0,1) or col==6 and row not in(0,1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


def while_m():
    """printing small 'm' using while loop"""
    i=0
    while i<6:
        j=0
        while j<8:
            if  j==0 or   i ==2 and   j not in(1,4,7)or   j==7 and   i in(3,4,5) or   j==4 and   i in(3,4):
            
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

