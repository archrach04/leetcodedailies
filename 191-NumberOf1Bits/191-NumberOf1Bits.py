# Last updated: 3/28/2026, 12:55:02 AM
class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res+=n%2
            n=n>>1
        
        return res
        