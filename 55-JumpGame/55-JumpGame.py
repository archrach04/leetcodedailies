# Last updated: 3/28/2026, 12:55:33 AM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        finalpos=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=finalpos:
                finalpos=i
            
        if finalpos==0:
            return True
        else:
            return False
        
        