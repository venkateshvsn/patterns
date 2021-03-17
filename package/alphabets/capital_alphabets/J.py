def for_J():
    """printing capital 'J' using for loop"""
    for row in range(6):
        for col in range(7):
            if row==0 or col==3 and row!=5 or row==5 and col in(1,2)or col==0 and row in(3,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_J():
    """printing capital 'J' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if i==0 or j==2 and i!=4 or i==3 and j not in(1,3,4)or i==4 and j==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

