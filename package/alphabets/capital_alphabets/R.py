def for_R():
    """printing capital 'R' using for loop"""
    for row in range(8):
        for col in range(5):
            if col==0 or col==4 and row not in(0,4) or row==0 and col in(1,2,3) or row==4 and col in(1,2,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        


def while_R():
    """printing capital 'R' using while loop"""
    i=0
    while i<7:
        j=0
        while j<5:
            if i==0 and j not in(0,4)or j==4 and i not in(0,4)or i==4 and j!=4or j==0:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

