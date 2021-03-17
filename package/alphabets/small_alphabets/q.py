def for_q():
    """printing small 'q' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==3 or col==0 and row in(2,3) or row==1 and col in(1,2) or row==4 and col in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_q():
    """printing small 'q' using while loop"""
    i=0
    while i<7:
        j=0
        while j<4:
            if j==0 and i ==2 or j==1 and i in(1,3) or j==3:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

