def for_ONE():
    """printing number 'ONE' using for loop"""
    for row in range(7):
        for col in range(5):
            if col==2 or row==6 or col==0 and row==2 or col==1 and row==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


def while_ONE():
    """printing number 'ONE' using while loop"""
    i=0
    while i<7:
        j=0
        while j<5:
            if j==2 or i==6 or i==1 and j==1:
            
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

