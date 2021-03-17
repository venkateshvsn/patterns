def for_h():
    """printing small 'h' using for loop"""
    for row in range(7):
        for col in range(5):
            if col==0 or col==4 and row in(4,5,6) or row==3 and col!=4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


def while_h():
    """printing small 'h' using while loop"""
    i=0
    while i<6:
        j=0
        while j<5:
            if j==0 or i==2 and j in (2,3)or j==4 and i not in(0,1,2):
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

