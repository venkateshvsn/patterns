def for_SEVEN():
    """printing number 'SEVEN' using for loop"""
    for row in range(7):
        for col in range(6):
            if col==3 or row==0 and col not in(4,5) or row==3 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_SEVEN():
    """printing number 'SEVEN' using while loop"""
    i=0
    while i<5:
        j=0
        while j<6:
            if j==3 or i==0 and j not in(4,5)or i==2:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

