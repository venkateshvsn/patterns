def for_u():
    """printing small 'u' using for loop"""
    for row in range(4):
        for col in range(4):
            if col==0 and row!=3 or col==3 and row!=3 or row==3 and col in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_u():
    """printing small 'u' using while loop"""
    i=0
    while i<3:
        j=0
        while j<4:
            if j==0and i!=2 or j==3 and i!=2 or i==2 and j in(1,2):
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

