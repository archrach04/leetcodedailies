# Last updated: 3/28/2026, 12:55:43 AM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            if nums[l]==val:
                if nums[r]!=val:
                    nums[l]=nums[r]
                    l+=1
                r-=1
            else:
                l+=1
        return l