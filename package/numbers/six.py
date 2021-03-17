def for_SIX():
    """printing number 'SIX' using for loop"""
    for row in range(6):
        for col in range(4):
            if col==0 and row in(3,4) or col==1 and row in(2,5) or col==2 and row in(1,3,4) or col==3 and row==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_SIX():
    """printing number 'SIX' using while loop"""
    i=0
    while i<6:
        j=0
        while j<4:
            if j==0 and i in(3,4)or j==1 and i in(2,5)or j==2 and i in(1,3,4)or j==3and i==0:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

