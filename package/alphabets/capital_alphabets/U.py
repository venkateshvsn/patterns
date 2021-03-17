def for_U():
    """printing capital 'U' using for loop"""
    for row in range(6):
        for col in range(5):
            if col==0 and row!=5 or col==4 and row!=5 or row==5 and col in(1,2,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_U():
    """printing capital 'U' using while loop"""
    i=0
    while i<5:
        j=0
        while j<4:
            if   j==0and   i!=4 or   j==3 and   i!=4 or   i==4 and   j not in(0,3) :
            
            
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

