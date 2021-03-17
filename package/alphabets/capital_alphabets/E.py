def for_E():
    """printing capital 'E' using for loop"""
    for row in range(5):
        for col in range(4):
            if row==0 or col==0 or row==2 or row==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_E():
    """printing capital 'E' using while loop"""
    i=0
    while i<5:
        j=0
        while j<4:
            if j==0 or i==0 or i==2 or i==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

