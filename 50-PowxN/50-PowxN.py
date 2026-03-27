# Last updated: 3/28/2026, 12:55:36 AM
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):

            if x==0: 
                return 0
            if n==0:
                return 1
            res=helper(x,n//2)
            res*=res
            return res*x if n%2 else res
        
        res=helper(x,abs(n))
        return 1/res if n<0 else res

            