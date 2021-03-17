def for_i():
    """printing small 'i' using for loop"""
    for row in range(6):
        for col in range(3):
            if col==1 or row==1 or row==5:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_i():
    """printing small 'i' using while loop"""
    i=0
    while i<6:
        j=0
        while j<3:
            if j==1 or j==0 and i in(2,5) or j==2 and i==5:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

