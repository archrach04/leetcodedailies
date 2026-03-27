# Last updated: 3/28/2026, 12:55:27 AM
class Solution:
    def climbStairs(self, n: int) -> int:
        one,two=1,1
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp
        return one
        