#MISSING NUMBER IN ARRAY GFG CODING QUESTION


for _ in range(int(input())):
    
    n = int(input())
    r = [int(x) for x in input().split()]
    
    s = (n*(n+1))/2
    
    s1 = sum(r)
    
    print(int(s-s1))
