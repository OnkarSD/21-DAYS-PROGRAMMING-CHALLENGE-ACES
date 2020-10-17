#ADITS SURVEY

n = int(input())
r = [int(x) for x in input().split()]

for i in r:
    if i*8 < 250:
        print(250,end=" ")
    else:
        print(i*8,end=" ")


#KARAN AND QUIZ

for _ in range(int(input())):
    
    n = int(input())
    r = [int(x) for x in input().split()]
    
    r = list(set(r))
    
    r = sorted(r)[::-1]
    
    
    if len(r) <= 1:
        print(-1)
    else:
        print(r[1])

#NISHNTS TREASURE

for _ in range(int(input())):
    
    a,b=[int(x) for x in input().split()]
    

    
    a = str("{:032b}".format(a))
    b = str("{:032b}".format(b))
    count = 0

    
    for i in range(0,len(a)):
        if a[i] != b[i]:
            count+=1
    print(count)


#ANUSHKAS ARRAY

for _ in range(int(input())):
    
    n = int(input())
    r = [x for x in input().split()]
    
    r = [0 if x=="X" else x for x in r]
    r = [1 if x=="Y" else x for x in r]
    
    
    m = 0
    cm = 0
    og = 0
    
    for i in range(n):
        
        if r[i] == 0:
            og +=1
        
        v = 1 if r[i] == 1 else -1
        
        cm = max(v,cm+v)
        m  = max(m,cm)
        
    print(og+m)
        


