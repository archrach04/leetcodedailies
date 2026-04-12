# Last updated: 4/12/2026, 8:29:11 PM
1class Solution:
2    def sortedSquares(self, nums: List[int]) -> List[int]:
3        for i in range(len(nums)):
4            nums[i]=nums[i]*nums[i]
5        nums.sort()
6        return nums
7        