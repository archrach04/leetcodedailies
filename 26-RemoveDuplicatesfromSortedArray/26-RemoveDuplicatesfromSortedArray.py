# Last updated: 8/2/2026, 5:09:25 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        j=1
4        
5        for i in range(1,len(nums)):
6            if nums[i]!=nums[i-1]:
7                nums[j]=nums[i]
8                j+=1
9        
10        return j
11        