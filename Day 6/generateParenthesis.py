#LEETCODE GENERATE PERENTHESIS PROBLEM

        def backtracking(res,s,opening, closing, n):
            if len(s)==n*2: 
                res.append(s)
                return
            
            if opening<n:
                backtracking(res, s+"(", opening+1, closing,n)
                
            if closing < opening: 
                backtracking(res, s+")", opening, closing+1,n)
                
        res=[]
        backtracking(res,"",0,0,n)
        return res

