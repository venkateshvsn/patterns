def for_Y():
    """printing capital 'Y' using for loop"""
    for row in range(7):
        for col in range(7):
            if col+row==6 or col==0 and row==0 or col==1 and row ==1 or col==2 and row==2:
                print("*",end=" ") 
            else:
                print(" ",end=" ")
        print()



def while_Y():
    """printing capital 'Y' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if j+i==4 or j==0 and i==0 or j==1 and i ==1:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

