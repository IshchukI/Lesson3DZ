triangleWidth = 5

for i in range(0, 2):
    for j in range(1, triangleWidth+1):
        if i == 0:
            print("*"*j)
        else:
            print("*"*(triangleWidth-j))

