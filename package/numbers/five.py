def for_FIVE():
    """printing small 'FIVE' using for loop"""
    for row in range(5):
        for col in range(4):
            if col==0 and row!=3 or col==3 and row!=1 or row==0 or row==2 or row==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        


def while_FIVE():
    """printing small 'FIVE' using while loop"""
    i=0
    while i<5:
        j=0
        while j<4:
            if   i==0 or   i==2 or   i==4 or   j==3 and   i in(0,2,3,4)or   j==0 and   i==1:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

