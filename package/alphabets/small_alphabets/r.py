def for_r():
    """printing small 'r' using for loop"""
    for row in range(6):
        for col in range(3):
            if col==0 or col==1 and row==1 or col==2 and row==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


def while_r():
    """printing small 'r' using while loop"""
    i=0
    while i<6:
        j=0
        while j<3:
            if j==0 or j==1 and i==2 or j==2 and i==1:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

