def for_SQUAR():
    """printing symbole 'SQUAR' using for loop"""
    for row in range(10):
        for col in range(10):
            if col+row>=9 or row+col<=9:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


def while_SQUAR():
    """printing symbole 'SQUAR' using while loop"""
    i=0
    while i<10:
        j=0
        while j<10:
            if j+i>=9 or i+j<=9:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        i+=1
        print()

