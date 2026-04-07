# Last updated: 4/8/2026, 12:31:04 AM
1class Solution:
2    def differenceOfSum(self, nums: List[int]) -> int:
3        els=0
4        dis=0
5        for i in nums:
6            els+=i
7            while i>0:
8                dis+=i%10
9                i=i//10
10
11        return abs(els-dis)
12
13        