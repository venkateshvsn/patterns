def for_H():
    """printing capital 'H' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==0 or col==3 or row==3:
                print("*",end=" ")
            else: 
                print(" ",end=" ")
        print()



def while_H():
    """printing capital 'H' using while loop"""
    i=0
    while i<5:
        j=0
        while j<4:
            if j==0 or i==2 or j==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

