# Last updated: 5/14/2026, 2:00:35 AM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        
4        for i in range(len(nums)):
5            if nums[i]<=0:
6                nums[i]=float('inf')
7        
8        for i in range(len(nums)):
9            if 1<=abs(nums[i])<=len(nums):
10                nums[(abs(nums[i])-1)]=-abs(nums[abs(nums[i])-1])
11        for i in range(len(nums)):
12            if nums[i]>0:
13                return i+1
14        
15        return len(nums)+1