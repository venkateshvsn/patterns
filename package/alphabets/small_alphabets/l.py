def for_l():
    """printing small 'l' using for loop"""
    for row in range(6):
        for col in range(5):
            if col==2 and row not in(0,5) or row==0 and col in(0,1) or row==5 and col in(3,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        



def while_l():
    """printing small 'l' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if j==2 and i not in(3,4) or i==3 and j in(1,3) or i==4 and j in(0,4): 
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

