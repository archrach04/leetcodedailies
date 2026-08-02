# Last updated: 8/2/2026, 6:19:10 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5
6        """
7
8        l=0
9        for r in range(len(nums)):
10            if nums[r]!=0:
11                nums[l],nums[r]=nums[r],nums[l]
12                l+=1
13        return nums
14
15
16        