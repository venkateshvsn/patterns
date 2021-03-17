def for_d():
    """printing small 'd' using for loop"""
    for row in range(7):
        for col in range(5):
            if col==4 or col==0 and row in(4,5) or row==3 and col in(1,2,3) or row==6 and col in(1,2,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_d():
    """printing small 'd' using while loop"""
    i=0
    while i<5:
        j=0
        while j<3:
            if j==0 and i==3 or j==1 and i in(2,4) or j==2:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

