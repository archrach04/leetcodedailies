# Last updated: 8/9/2026, 7:46:18 PM
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        l,r=0,0
4        mlen=float('inf')
5        summ=0
6
7       
8        while r<len(nums):
9            summ+=nums[r]
10            while summ>=target:
11                mlen=min(mlen,r-l+1)
12                summ-=nums[l]
13                l+=1
14
15
16            r+=1
17            
18        return 0 if mlen==float('inf') else mlen
19
20
21
22        