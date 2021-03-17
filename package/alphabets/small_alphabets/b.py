def for_b():
    """printing small 'b' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==0 or row==3 and col!=3 or row==6 and col!=3 or col==3 and row in(4,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_b():
    """printing small 'b' using while loop"""
    i=0
    while i<7:
        j=0
        while j<4:
            if j==0 and i!=6 or i==3 and j!=3 or i==6 and j in (1,2) or j==3 and i in(4,5):
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

