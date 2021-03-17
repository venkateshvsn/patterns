def for_o():
    """printing small 'o' using for loop"""
    for row in range(4):
        for col in range(4):
            if col==0 and row in(1,2) or col==3 and row in(1,2) or row==0 and col in(1,2) or row==3 and col in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_o():
    """printing small 'o' using while loop"""
    i=0
    while i<4:
        j=0
        while j<4:
            if j==0 and i in(1,2)or j==3 and i in(1,2)or i==0 and j in(1,2)or i==3 and j in(1,2):
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

