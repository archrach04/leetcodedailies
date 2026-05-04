# Last updated: 5/4/2026, 9:52:07 PM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        hp=[]
4        for i in points:
5            dis=i[0]**2+i[1]**2
6            if len(hp)<k:
7                heapq.heappush(hp,(-dis,[i[0],i[1]]))
8            else:
9                if hp[0][0]<-dis:
10                    heapq.heappop(hp)
11                    heapq.heappush(hp,(-dis,[i[0],i[1]]))
12        res=[]
13        for i in hp:
14            res.append(i[1])
15        
16        return res
17        
18
19
20
21        