# Last updated: 5/7/2026, 11:02:31 PM
1class Solution:
2    def longestSubarray(self, nums: List[int]) -> int:
3
4        start=0
5        max_len=0
6        zero=-1
7
8        for r in range(len(nums)):
9            if nums[r]==0:
10                maxnow=0
11                start=zero+1
12                zero=r
13
14            maxnow=r-start
15            max_len=max(max_len,maxnow)
16        return max_len
17           
18        
19
20
21        