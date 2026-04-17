# Last updated: 4/17/2026, 10:12:35 AM
1class Solution:
2    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
3        maxh=[]
4        for i in arr:
5            if len(maxh)<k:
6                heapq.heappush(maxh,(-abs(x-i),-i))
7            else:
8                if maxh[0]<(-abs(x-i),-i):
9                    heapq.heappop(maxh)
10                    heapq.heappush(maxh,(-abs(x-i),-i))
11        return sorted([-num for dist, num in maxh])
12        