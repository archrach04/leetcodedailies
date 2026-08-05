# Last updated: 8/5/2026, 11:19:55 PM
1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        currtot=sum(nums[:k])
4        max_sub=sum(nums[:k])
5        l=0
6        for r in range(k,len(nums)):
7            currtot+=-nums[l]+nums[r]
8            max_sub=max(currtot,max_sub)
9            l+=1
10        
11        return max_sub/k
12
13            
14        
15
16
17        
18
19        