
#UNDERSTANDING KADANES PRINCIPLE

for _ in range(int(input())):
    n = int(input())
    r = [int(x) for x in input().split()]
    
    max_so_far = r[0] 
    max_ending_here = 0
       
    for i in range(0, n): 
        max_ending_here = max_ending_here + r[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
        if max_ending_here < 0: 
            max_ending_here = 0   
    print(max_so_far) 

