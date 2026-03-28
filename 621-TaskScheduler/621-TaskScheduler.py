# Last updated: 3/28/2026, 9:35:05 PM
1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3        counter=Counter(tasks)
4        maxHeap=[-cnt for cnt in counter.values()]
5        heapq.heapify(maxHeap)
6
7        time=0
8        q=deque()
9        while maxHeap or q:
10            time+=1
11            if maxHeap:
12                cnt=1+heapq.heappop(maxHeap)
13                if cnt:
14                    q.append([cnt,time+n])
15            if q and q[0][1]==time:
16                heapq.heappush(maxHeap,q.popleft()[0])
17        return time
18        