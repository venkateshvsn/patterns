def for_TWO():
    """printing number 'TWO' using for loop"""
    for row in range(6):
        for col in range(4):
            if col==0 and row !=2 or col==3 and row!=4 or row==0 or row==3 or row==5:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_TWO():
    """printing number 'TWO' using while loop"""
    i=0
    while i<6:
        j=0
        while j<4:
            if   i==0 or   i==3 or   i==5 or   j==0 and   i!=2 or  j ==3 and i!=4:
            
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

