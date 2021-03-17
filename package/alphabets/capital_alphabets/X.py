def for_X():
    """printing capital 'X' using for loop"""
    for row in range(7):
        for col in range(7):
            if col-row==0 or col+row==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print(" ")



def while_X():
    """printing capital 'X' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if j-i==0 or j+i==4:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

