def for_f():
    """printing small 'f' using for loop"""
    for row in range(7):
        for col in range(5):
            if col==1 and row!=0  or row==0 and col in(2,3) or col==4 and row==1 or row==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_f():
    """printing small 'f' using while loop"""
    i=0
    while i<7:
        j=0
        while j<4:
            if j==1 and i!=0 or i==0 and j in(2,3)or i==3 and j!=3 :
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

