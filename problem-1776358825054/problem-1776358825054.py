# Last updated: 4/16/2026, 10:30:25 PM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        minh=[]
4        for i in nums:
5            if len(minh)<k:
6                heapq.heappush(minh,i)
7            else:
8                if i>minh[0]:
9                    heapq.heappop(minh)
10                    heapq.heappush(minh,i)
11        
12        return minh[0]
13