def for_B():
    for row in range(7):
        """printing capital 'B' using for loop"""
        for col in range(4):
            if col==0 or row==0 and col!=3 or row==3 and col!=3 or row==6 and col!=3 or col==3 and row in(1,2,4,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        


def while_B():
    """printing capital 'B' using while loop"""
    i=0
    while i<7:
        j=0
        while j<5:
            if j==0 or i==0 and j!=4 or i==3 and j!=4 or i==6 and j!=4or j==4 and i%3!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

