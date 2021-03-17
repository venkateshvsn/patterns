def for_V():
    """printing capital 'V' using for loop"""
    for row in range(5):
        for col in range(10):
            if col-row==0 or col+row==8:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_V():
    """printing capital 'V' using while loop"""
    i=0
    while i<4:
        j=0
        while j<7:
            if i-j==0 or j==4 and i==2 or j==5 and i==1 or j==6 and i==0:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

