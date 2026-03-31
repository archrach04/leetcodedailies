# Last updated: 3/31/2026, 11:16:35 PM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        hs={}
4        for i in nums:
5            if i in hs:
6                hs[i]+=1
7            else:
8                hs[i]=1
9        for j in hs:
10            if hs[j]==1:
11                return j