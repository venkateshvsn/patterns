def for_n():
    """printing small 'n' using for loop"""
    for row in range(6):
        for col in range(4):
            if col==0 or col==3 and row not in (0,1) or row==1 and col!=3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


def while_n():
    """printing small 'n' using while loop"""
    i=0
    while i<6:
        j=0
        while j<6:
            if j==0 and i==0 or j==1and i!=0 or j==5 and i in(3,4,5)or i==2 and j in(3,4):
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

