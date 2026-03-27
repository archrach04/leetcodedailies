# Last updated: 3/28/2026, 12:55:30 AM
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[]
        for i in range(m):
            dp.append([0]*n)
        for column in range(n):
            dp[0][column]=1
        for row in range(m):
            dp[row][0]=1
        for row in range(1,m):
            for column in range(1,n):
                dp[row][column]+=dp[row-1][column]+dp[row][column-1]
        
        return dp[m-1][n-1]

        
        