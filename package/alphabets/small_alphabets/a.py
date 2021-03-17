def for_a():
    """printing small 'a' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==3 and row!=0 or col==0 and row not in(0,2,3,6) or row==3 and col in(1,2)  or row==6 and col in(1,2) or row==0 and col in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_a():
    """printing small 'a' using while loop"""
    i=0
    while i<4:
        j=0
        while j<6:
            if j==0 and i in (1,2) or i==0 and j in(1,2) or j==3 and i in(1,2) or i==3 and j in(1,2,4) or j==5 and i==2:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

