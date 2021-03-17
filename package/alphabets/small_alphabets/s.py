def for_s():
    """printing small 's' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==0 and row not in(0,3,4,6) or col==3 and row not in(0,2,3,6) or row==0 and col in(1,2) or row==3 and col in(1,2) or row==6 and col in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


def while_s():
    """printing small 's' using while loop"""
    i=0
    while i<6:
        j=0
        while j<4:
            if j==3 and i==3 or j==2 and i in(0,2,4)or j==1 and i in(0,2,4) or j==0 and i==1:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

