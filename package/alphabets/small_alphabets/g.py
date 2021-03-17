def for_g():
    """printing small 'g' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==0 and row not in(0,3,4,6) or col==3 and row not in(0,6) or row==0 and col in(1,2) or row==3 and col in(1,2) or row==6 and col in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_g():
    """printing small 'g' using while loop"""
    i=0
    while i<9:
        j=0
        while j<4:
            if j==0 and i in(2,3,6)or j==1 and i in (1,4,7)or j==2 and i in (1,4,7)or j==3 and i not in(7,8):
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

