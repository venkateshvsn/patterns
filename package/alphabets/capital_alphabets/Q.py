def for_Q():
    """printing capital 'Q' using for loop"""
    for row in range(5):
        for col in range(6):
            if col==0 and row not in(0,4) or col==4 and row not in(0,4) or row==0 and col in(1,2,3)or row==4 and col not in(0,4) or row==2 and col==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_Q():
    """printing capital 'Q' using while loop"""
    i=0
    while i<5:
        j=0
        while j<6:
            if j==0and i not in(0,4) or i==0 and j not in(0,4,5)or i==4 and j not in(0,4)or j==4 and i not in(0,4)or j==2 and i==2:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

