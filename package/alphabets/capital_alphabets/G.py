def for_G():
    """printing capital 'G' using for loop"""
    for row in range(6):
        for col in range(5):
            if col==0 and row not in(0,5) or row==0 and col in(1,2,3) or row==5 and col not in(0,4) or row==3 and col!=1 or col==4 and row in(1,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_G():
    """printing capital 'G' using while loop"""
    i=0
    while i<6:
        j=0
        while j<6:
            if j==0 and i not in(0,4,5) or i==0 and j not in(0,4,5) or i==1 and j not in(1,2,3,4,5)or i==2 and j not in(1,2)or i==3 and j not in(1,2,4)or i==4 and j not in(1,2,4) or i==5 and j not in(0,3,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

