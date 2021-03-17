def for_THREE():
    """printing small 'THREE' using for loop"""
    for row in range(5):
        for col in range(4):
            if row==0 or row==2 or row==4 or col==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_THREE():
    """printing small 'THREE' using while loop"""
    i=0
    while i<5:
        j=0
        while j<4:
            if i==0 or i==4 or j==3 or i==2:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

