maximum = 5
rows = 2*maximum
for x in range(1,rows):
    if x<=maximum:
        for x in range(0,x):
            print("*",end="")
        print("\r")
    else:
        for x in range(rows-x,0,-1):
            print("*",end="")
        print("\r")

