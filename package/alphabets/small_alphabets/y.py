def for_y():
    """printing small 'y' using for loop"""
    for row in range(6):
        for col in range(3):
            if col==2 and row!=5 or col==0 and row in(0,4) or col==1 and row in(1,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
for_y()


def while_y():
    """printing small 'y' using while loop"""
    i=0
    while i<5:
        j=0
        while j<3:
            if j==2 and i!=4 or j==1 and i in(1,4)or j==0 and i in(0,3) :
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()
while_y()
