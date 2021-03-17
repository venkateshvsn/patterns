def for_P():
    """printing capital 'P' using for loop"""
    for row in range(10):
        for col in range(5):
            if col==0 or col==4 and row in(1,2,3)or row==0 and col in(1,2,3)or row==4 and col in(1,2,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        


def while_P():
    """printing capital 'P' using while loop"""
    i=0
    while i<8:
        j=0
        while j<5:
            if i==0 and j not in(0,4)or j==4 and i not in(0,4,5,6,7)or i==4 and j!=4or j==0 :
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

