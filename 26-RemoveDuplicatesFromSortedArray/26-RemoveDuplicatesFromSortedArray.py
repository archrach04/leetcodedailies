# Last updated: 3/28/2026, 12:55:44 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[j]=nums[i]
                j+=1
        return j
        