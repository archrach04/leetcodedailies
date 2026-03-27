# Last updated: 3/28/2026, 12:54:44 AM
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        offset=1      
        for i in range(1,n+1):
            if offset*2==i:
                offset=i
            dp[i]=1+dp[i-offset]
        return dp