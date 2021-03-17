def for_A():
    """printing capital 'A' using for loop"""
    for row in range(4):
        for col in range(7):
            if row+col==3 or row-col==-3 or row==2 and col in(2,3,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_A():
    """printing capital 'A' using while loop"""
    i=0
    while i<4:
        j=0
        while j<7:
            if i+j==3 or i-j==-3 or i==2 and j in(2,3,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

