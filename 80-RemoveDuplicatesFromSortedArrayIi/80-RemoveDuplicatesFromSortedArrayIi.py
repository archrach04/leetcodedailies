# Last updated: 3/28/2026, 12:55:25 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        replace=2
        if len(nums)<2:
            return len(nums)
        for i in range(2,len(nums)):
            if nums[i]!=nums[replace-2]:
                nums[replace]=nums[i]
                replace+=1
        
        return replace