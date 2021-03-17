def for_C():
    """printing capital 'C' using for loop"""
    for row in range(4):
        for col in range(4):
            if col==0 and row not in(0,3) or row==0 and col!=0 or row==3 and col!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_C():
    """printing capital 'C' using while loop"""
    i=0
    while i<5:
        j=0
        while j<4:
            if j==0 and i not in(0,4)  or i==0 and j!=0 or  i==4 and j!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

