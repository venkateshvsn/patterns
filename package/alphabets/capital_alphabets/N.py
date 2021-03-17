def for_N():
    """printing capital 'N' using for loop"""
    for row in range(5):
        for col in range(5):
            if col==0 or col==4 or col-row==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_N():
    """printing capital 'N' using while loop"""
    i=0
    while i<4:
        j=0
        while j<4:
            if j==0 or j==3 or j==1 and i==1 or j==2 and i==2:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

