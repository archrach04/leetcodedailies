# Last updated: 7/30/2026, 8:23:36 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        res=[]
4        nums.sort()
5        for i in range(len(nums)-2):
6            if i>0 and nums[i]==nums[i-1]:
7                continue
8            
9            low=i+1
10            high=len(nums)-1
11
12            while low<high:
13                tot=nums[i]+nums[low]+nums[high]
14
15                if tot>0:
16                    high-=1
17                elif tot<0:
18                    low+=1
19                else:
20                    t=[nums[i],nums[high],nums[low]]
21                    res.append([nums[i],nums[high],nums[low]])
22                    low+=1
23                    high-=1
24
25                    while low<high and nums[low]==nums[low-1]:
26                        low+=1
27                    while low<high and nums[high]==nums[high+1]:
28                        high-=1
29        return res
30        