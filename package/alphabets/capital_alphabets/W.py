def for_W():
    """printing capital 'W' using for loop"""
    for row in range(7):
        for col in range(7):
            if col==0  or col==6 or row==3 and col==3 or row==4 and col in(2,4) or row==5 and col in(1,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


def while_W():
    """printing capital 'W' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if j==0 or j==4 or i==3 and j in(1,3) or i==2 and j==2:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

