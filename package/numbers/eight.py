def for_EIGHT():
    """printing small 'EIGHT' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==0 and row not in(0,3,6) or col==3 and row not in(0,3,6) or row==0 and col in(1,2) or row==3 and col in(1,2) or row==6 and col in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        

def while_EIGHT():
    """printing small 'EIGHT' using while loop"""
    i=0
    while i<7:
        j=0
        while j<5:
            if j==0 and i not in(0,3,6) or j==4and i not in(0,3,6) or j==2 and i in(0,3,6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

