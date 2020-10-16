
#NUMBER OF 2S IN A RANGE

def number0f2s(n):
    n = str(n)
    ct = n.count("2")
    return ct
    
    #add Code here
    
def numberOf2sinRange(n):
    
    #add code here
    
    t = 0
    
    for i in range(2,n+1):
        t += number0f2s(i)
    return t


