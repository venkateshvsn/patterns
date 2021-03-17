def for_w():
    """printing small 'w' using for loop"""
    for row in range(6):
        for col in range(7):
            if col==0  and row!=5 or col==3 and row in(3,4) or col==6 and row!=5 or row==5 and col not in(0,3,6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_w():
    """printing small 'w' using while loop"""
    i=0
    while i<4:
        j=0
        while j<5:
            if j==0 and i!=3 or j==4 and i!=3or i==3 and j in(1,3)or j==2 and i ==2:
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

