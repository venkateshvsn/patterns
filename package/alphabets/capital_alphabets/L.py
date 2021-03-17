def for_L():
    """printing capital 'L' using for loop"""
    for row in range(7):
        for col in range(5):
            if col==0 or row==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_L():
    """printing capital 'L' using while loop"""
    i=0
    while i<4:
        j=0
        while j<4:
            if j==0 or i==3:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

