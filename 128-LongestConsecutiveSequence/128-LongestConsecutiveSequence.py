# Last updated: 3/28/2026, 12:55:15 AM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set()
        maxm=0
        for i in range(len(nums)):
            if nums[i] not in numSet:
                numSet.add(nums[i])
        for num in numSet:
            if num-1 not in numSet:
                length=0
                while num+length in numSet:
                    length+=1
                    maxm=max(maxm,length)
        return maxm
        