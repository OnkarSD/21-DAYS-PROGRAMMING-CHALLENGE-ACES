#983. Minimum cost of ticket

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [None]*n
        
        def func(i):
            if i>=n: return 0
            
            if dp[i]: return dp[i]
            a,b,c = i+1,i+1,i+1
            
            while b<n and days[b]<=days[i]+6:
                b+=1
            while c<n and days[c]<=days[i]+29:
                c+=1
            
            dp[i] = min(costs[0]+func(a),costs[1]+func(b),costs[2]+func(c))
            return dp[i]
       
        return func(0)
