def for_t():
    """printing small 't' using for loop"""
    for row in range(6):
        for col in range(4):
            if col==1 or row==1 or row==5 and col!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_t():
    """printing small 't' using while loop"""
    i=0
    while i<5:
        j=0
        while j<4:
            if j==1and i!=4 or i==2 or i==4 and j in (2,3):
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

