# Last updated: 4/20/2026, 5:30:21 PM
1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        result=[]
4        n=len(intervals)
5        i=0
6        while i<n and intervals[i][1]<newInterval[0]:
7            result.append(intervals[i])
8            i+=1
9        while i<n and intervals[i][0]<=newInterval[1]:
10            newInterval[0]=min(newInterval[0],intervals[i][0])
11            newInterval[1]=max(newInterval[1],intervals[i][1])
12            i+=1
13        result.append(newInterval)
14
15        while i<n: 
16            result.append(intervals[i])
17            i+=1
18            
19        return result
20            
21
22
23
24        