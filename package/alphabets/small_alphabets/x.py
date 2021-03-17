def for_x():
    """printing small 'x' using for loop"""
    for row in range(5):
        for col in range(5):
            if col-row==0 or col+row==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_x():
    """printing small 'x' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if j==0 and i in(1,3) or j==1 and i in(1,3)or j==2 and i==2 or j==3 and i in(1,3)or j==4and i in(1,3):
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

