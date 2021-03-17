def for_TEN():
    """printing small 'TEN' using for loop"""
    for row in range(6):
        for col in range(7):
            if col==0 and row in(1,5) or col==1 or col==2 and row==5 or col==3 and  row not in(0,5) or col==6 and row not in(0,5) or row==0 and col in(4,5) or row==5 and col in(4,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_TEN():
    """printing small 'TEN' using while loop"""
    i=0
    while i<5:
        j=0
        while j<7:
            if j==0 and i in(1,4)or j==1 or j==2 and i==4 or j==3 and i not in(0,4)or j==4 and i in(0,4)or j==5 and i in(0,4)or j==6 and i not in(0,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

