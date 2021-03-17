def for_NINE():
    """printing number 'NINE' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==3 or row==0 and col in(1,2) or row==3 and col in(1,2) or col==0 and row in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_NINE():
    """printing number 'NINE' using while loop"""
    i=0
    while i<7:
        j=0
        while j<5:
            if j==0 and i in(1,2)or i==0 and j not in(0,4) or i==3and j!=0 or j==4 and i!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

