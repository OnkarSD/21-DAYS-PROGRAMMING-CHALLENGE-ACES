import math
def withLog2(x):
    return False if x == 0 else (math.log10(x)/math.log10(2))
def isIn2(n):
    return (math.ceil(withLog2(n)) == math.floor(withLog2(n)))
tc = int(input())
for x in range(tc):
    n = int(input())
    if n==1:
        print(1)
    elif isIn2(n):
        print(-1)
    elif n==5:
        print(2," ",3," ",1," ",5," ",4)
    elif n==3:
        print(1," ",3," ",2)
    else:
        print(2," ",3," ",1," ",5," ",4,end=" ")
        i = 6
        while(i<=n):
            if isIn2(i):
                print(" ",i+1," ",i,end=" ")
                i=i+2
            else:
                print(" ",i,end=" ")
                i=i+1
