def for_HEART():
    """printing symbole 'HEART' using while loop"""
    for row in range(6):
        for col in range(7):
            if row in(1,2) or row==0 and col%3!=0 or row==3 and col not in(0,6) or row==4 and col in(2,3,4) or col==3 and row in (5,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_HEART():
    """printing symbole 'HEART' using while loop"""
    i=0
    while i<6:
        j=0
        while j<7:
            if i in(1,2) or i==0 and j%3!=0 or i==3 and j not in(0,6) or i==4 and j in(2,3,4) or j==3 and i in (5,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

