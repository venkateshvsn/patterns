def for_FOUR():
    """printing small 'FOUR' using for loop"""
    for row in range(5):
        for col in range(4):
            if col==2 or row==2 or col==1 and row==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_FOUR():
    """printing small 'FOUR' using while loop"""
    i=0
    while i<5:
        j=0
        while j<4:
            if i==2 or j==2 or j==1 and i in(1,2):
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

