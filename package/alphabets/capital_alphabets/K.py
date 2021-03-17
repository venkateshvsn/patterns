def for_K():
    """printing capital 'K' using for loop"""
    for row in range(9):
        for col in range(5):
            if row+col==4 or row-col==4 or col==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_K():
    """printing capital 'K' using while loop"""
    i=0
    while i<5:
        j=0
        while j<4:
            if j==0  or j==1 and i not in(0,1,3,4)or j==2 and i not in(0,2,4)or j==3 and i not in(1,2,3):
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

