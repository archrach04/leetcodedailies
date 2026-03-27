# Last updated: 3/28/2026, 12:55:09 AM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMax=1
        curMin=1

        for n in nums:
            if n==0:
                curMax=1
                curMin=1
            temp=curMax
            curMax=max(curMax*n,curMin*n,n)
            curMin=min(temp*n,curMin*n,n)

            res=max(res, curMax)
        return res

        