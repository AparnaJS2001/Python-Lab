n=5
for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print(" ")
m=4       
for i in range(m + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")    
