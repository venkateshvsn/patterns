def for_M():
    """printing capital 'M' using for loop"""
    for row in range(5):
        for col in range(5):
            if col==0 or col==4 or row==1 and col in(1,3) or row==2 and col==2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
for_M()


def while_M():
    """printing capital 'M' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if j==0 or j==4 or j==1 and i==1 or j==2 and i==2 or j==3 and i==1:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()
while_M()
