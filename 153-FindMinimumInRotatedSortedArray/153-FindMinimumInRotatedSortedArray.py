# Last updated: 3/28/2026, 12:55:08 AM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        res=float('inf')

        while low<=high:
            mid=(low+high)//2

            if nums[low]<=nums[mid]:
                res=min(res,nums[low])
                low=mid+1
            else:
                res=min(res,nums[mid])
                high=mid-1

        return res
        

        