def for_T():
    """printing capital 'T' using for loop"""
    for row in range(7):
        for col in range(7):
            if row==0 or col==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_T():
    """printing capital 'T' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if i==0 or j==2:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

