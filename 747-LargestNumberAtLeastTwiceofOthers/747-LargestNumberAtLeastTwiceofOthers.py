# Last updated: 4/14/2026, 10:46:39 AM
1class Solution:
2    def dominantIndex(self, nums: List[int]) -> int:
3        n=float("-inf")
4        ind=0
5        for i in range(len(nums)):
6            if nums[i]>n:
7                n=nums[i]
8                ind=i
9        for i in nums:
10            if i==n:
11                continue
12            if n<i*2:
13                return -1
14        return ind
15        