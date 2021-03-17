def for_c():
    """printing small 'c' using for loop"""
    for row in range(5):
        for col in range(5):
            if row==0 and col not in(0,4) or row==4 and col not in(0,4) or col==0 and row not in(0,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_c():
    """printing small 'c' using while loop"""
    i=0
    while i<4:
        j=0
        while j<4:
            if j==0 and i in(1,2) or i==0 and j!=0 or i==3 and j!=0:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

