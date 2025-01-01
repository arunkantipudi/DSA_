def pattern1(n):
    for i in range(n):
        print(" * "*n)
    # or
    # for i in range(n):
    #     for j in range(n):
    #         print(" * ",end="")
    #     print()
def pattern2(n):
    for i in range(1,n+1):
        print(" * "*(i))
    # or
    # for i in range(1,n+1):
    #     for j in range(i):
    #         print(" * ",end="")
    #     print()
def pattern3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
def pattern4(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end="")
        print()
def pattern5(n):
    for i in range(n,0,-1):
        print("*"*i)
    # or 
    # for i in range(n,0,-1):
    #     for j in range(i):
    #         print("*",end="")
    #     print()
def pattern6(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end="")
        print()



    for i in range(n-1,-1,-1):
        for j in range(i):
            print("* ",end="")
        print()    
def pattern7(n):

    for i in range(n):
        # to add space befor stars
        for j in range(n-i-1):
            print(" ",end="")

        # to print stars
        for j in range(2*i+1):
            print("*",end="")

        # agian to add space after stars
        for j in range(n-i-1):
            print(" ",end="")
        
        # after each line printed to move to next lin print() is used
        print()
def pattern8(n):
    # this is exactly reverse to the pattern 7 so just changed the range of i into reverse format
    for i in range(n-1,-1,-1):
        for j in range(n-i-1):
            print(" ",end="")

        # to print stars
        for j in range(2*i+1):
            print("*",end="")

        # agian to add space after stars
        for j in range(n-i-1):
            print(" ",end="")
        
        # after each line printed to move to next lin print() is used
        print()
def pattern9(n):
    # this is the combination of both pattern 7 and 8 so we can use the same logic here
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end = "")
        for j in range(2*i+1):
            print("*",end= "")
        for j in range(n-i-1):
            print(" ",end = "")
        print()
    for i in range(n-1,-1,-1):
        for j in range(n-i-1):
            print(" ",end = "")
        for j in range(2*i+1):
            print("*",end= "")
        for j in range(n-i-1):
            print(" ",end = "")
        print()
def pattern10(n):
    for i in range(1,n+1):
        for j in range(i):
            print("* ",end="")
        print()
def pattern11(n):
    start = 1
    for i in range(1,n+1):
        if i%2 == 1: start = 1
        else: start = 0
        for j in range(i):
            print(start,end="")
            start = 1-start
        print()
def pattern12(n):
    for i in range(n):
        for j in range(1,i+1):
            print(j,end="")
        for j in range(2*n-2*(i+1)):
            print(" ",end="")
        for j in range(i,0,-1):
            print(j,end="")
        print()
def pattern13(n):
    ans = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            ans +=1
            print(f" {ans} ",end="")
        print()
def pattern14(n):
    for i in range(1, n + 1):
        for j in range(i):
            # ord for converting the character to ascii value
            # char is to convert ascii into char
            print(chr(ord('A') + j), end="")
        print()
def pattern15(n):
    for i in range(n,-1,-1):
        for j in range(i):
            # ord for converting the character to ascii value
            # char is to convert ascii into char
            print(chr(ord('A') + j), end="")
        print()
def pattern16(n):
    for i in range(n):
        print(chr(ord('A')+i)*(i+1))
def pattern17(n):
    for i in range(n-1):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i-i):
            print(chr(ord('A')+j),end="")   
        for j in range(i,-1,-1):
            print(chr(ord('A')+j),end="")
        print() 
def pattern18(n):
    for i in range(n,0,-1):
        for j in range(i-1,n):
            print(chr(ord('A')+j),end="")
        print()
def pattern19(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        for j in range(i*2):
            print(" ",end="")
        for j in range(n-i):
            print("*",end="")
        print()
    for i in range(n-1,-1,-1):
        for j in range(n-i):
            print("*",end="")
        for j in range(i*2):
            print(" ",end="")
        for j in range(n-i):
            print("*",end="")
        print()
        # or
        # for i in range(n):
        #     stars = "*" * (n - i)
        #     spaces = " " * (i * 2)
        #     print(stars + spaces + stars)
        
        # for i in range(n - 1, -1, -1):
        #     stars = "*" * (n - i)
        #     spaces = " " * (i * 2)
        #     print(stars + spaces + stars)
def pattern20(n):
    for i in range(n):
        stars = "*"*(i+1)
        space = " "*2*(n-i-1)
        print(stars+space+stars)
    for i in range(n-2,-1,-1):
        stars = "*"*(i+1)
        space = " "*2*(n-i-1) 
        print(stars+space+stars)
def pattern21(n):
    for i in range(n):
        if i == 0 or i == n - 1:  # First or last row
            print("*" * n)  # Print n stars
        else:  # Middle rows
            for j in range(n):
                if j == 0 or j == n - 1:  # First or last column
                    print("*", end="")
                else:  # Spaces in the middle
                    print(" ", end="")
            print()  # Move to the next line

# n = int(input("Entet a number = "))
pattern21(5)
