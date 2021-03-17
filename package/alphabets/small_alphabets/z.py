def for_z():
    """printing small 'z' using for loop"""
    for row in range(5):
        for col in range(5):
            if col+row==4 or row==0 or row==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_z():
    """printing small 'z' using while loop"""
    i=0
    while i<4:
        j=0
        while j<4:
            if j+i==3 or i==0 or i==3:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

