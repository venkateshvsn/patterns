def for_D():
    """printing capital 'D' using for loop"""
    for row in range(4):
        for col in range(4):
            if col==0 or row==0 and col!=3 or row==3 and col!=3 or col==3 and row in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_D():
    """printing capital 'D' using while loop"""
    i=0
    while i<4:
        j=0
        while j<4:
            if j==0 or i==0 and j!=3 or i==3 and j!=3 or j==3 and i%3!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()
   
        
