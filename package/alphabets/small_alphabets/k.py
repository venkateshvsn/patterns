def for_k():
    """printing small 'k' using for loop"""
    for row in range(7):
        for col in range(4):
            if col+row==3 or col-row==-3 or col==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_k():
    """printing small 'k' using while loop"""
    i=0
    while i<7:
        j=0
        while j<3:
            if j==0 or j==1 and i in (2,4) or j==2 and i in(1,5):
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

