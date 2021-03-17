
def for_OCTAGON():
    """printing symbole 'OCTAGON' using while loop"""
    for row in range(7):
        for col in range(7):
            if col in(2,3,4) or row in(2,3,4) or row in(1,5) and col not in(0,6):
                    print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
f




def while_OCTAGON():
    """printing symbole 'OCTAGON' using while loop"""
    i=0
    while i<7:
        j=0
        while j<7:
            if j in(2,3,4) or i in(2,3,4) or i in(1,5) and j not in(0,6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()
w
