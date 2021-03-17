
def for_DIAMAND():
    """printing symbole 'DIAMAND' using for loop"""
    for row in range(7):
        for col in range(7):
            if col==3 or row==3 or col in(2,4) and row not in(0,6) or row in(2,4) and col not in(0,6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


def while_DIAMAND():
    """printing symbole 'DIAMAND' using while loop"""
    i=0
    while i<7:
        j=0
        while j<7:
            if j==3 or i==3 or j in(2,4) and i not in(0,6) or i in(2,4) and j not in(0,6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

