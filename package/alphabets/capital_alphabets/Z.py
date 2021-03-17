def for_Z():
    """printing capital 'Z' using for loop"""
    for row in range(7):
        for col in range(7):
            if col+row==6 or row==0 or row==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_Z():
    """printing capital 'Z' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if j+i==4 or i==0 or i==4 :
            
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

