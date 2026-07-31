# Last updated: 7/31/2026, 10:33:10 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        slow=0
4        fast=0
5
6        while True:
7            slow=nums[slow]
8            fast=nums[nums[fast]]
9            if slow==fast:
10                break
11        
12        slow=0
13        while slow!=fast:
14            slow=nums[slow]
15            fast=nums[fast]
16        
17        return slow
18        
19        