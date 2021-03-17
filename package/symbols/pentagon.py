
def for_PENTAGON():
    """printing symbole 'PENTAGON' using for loop"""
    for row in range(7):
        for col in range(9):
            if col==4 or col in(3,5) and row!=0 or col in(2,6) and row not in(0,1) or row==4 or row in(3,5) and col not in(0,8):
                    print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_PENTAGON():
    """printing symbole 'PENTAGON' using while loop"""
    i=0
    while i<7:
        j=0
        while j<9:
            if j==4 or j in(3,5) and i!=0 or j in(2,6) and i not in(0,1) or i==4 or i in(3,5) and j not in(0,8):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

