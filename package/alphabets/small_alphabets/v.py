def for_v():
    """printing small 'v' using for loop"""
    for row in range(4):
        for col in range(7):
            if col-row==0 or col+row==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_v():
    """printing small 'v' using while loop"""
    i=0
    while i<3:
        j=0
        while j<7:
            if j-i==0 or j+i==4:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

