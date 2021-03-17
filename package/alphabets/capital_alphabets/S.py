def for_S():
    """printing capital 'S' using for loop"""
    for row in range(9):
        for col in range(5):
            if col==0 and row not in(0,4,5,8) or col==4 and row not in(0,3,4,8) or row==0 and col in(1,2,3) or row==4 and col in(1,2,3) or row==8 and col in(1,2,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_S():
    """printing capital 'S' using while loop"""
    i=0
    while i<10:
        j=0
        while j<6:
            if j==0 and i not in(0,5,6,9) or i==0  and j not in(0,5) or i==9and j not in(0,5) or i==5 and j not in(0,5) or j==5and i not in(0,3,4,5,9):

            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

