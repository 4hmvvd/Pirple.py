
def RowColumn():
    print("This program draws a playing board")
    print("NOTE: The input of row and column must be same and an odd number")
    row = int(input("\nEnter the value of row: "))
    column = int(input("Enter the value of column: "))

    for i in range(row):
        if i%2 == 0:
            for num in range(1,row+1):
                if num%2 == 1:
                    if num != row:
                        print(" ", end="")
                    else:
                        print(" ")
                
                else:
                    print("|",end="")
        else:
            print("-"*row)
    print()
    if row <= 81:
        return True
    else:
        return False
